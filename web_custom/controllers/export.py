import boto3
from botocore.config import Config
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from werkzeug.exceptions import InternalServerError

from odoo import http
from odoo.addons.web.controllers.export import ExcelExport
import json
import pandas as pd
import os
from odoo.http import request, _logger
from dotenv import load_dotenv
load_dotenv()
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')

aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
bucket_s3 = os.getenv('BUCKET')
s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name='ap-southeast-2',
                  config=Config(signature_version='s3v4'))

def upload_file_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        with open(file_name, "rb") as f:
            response = s3.put_object(Bucket=bucket, Key=object_name, Body=f)
        return response
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials provided")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    return True


class CustomExcelExport(ExcelExport):

    @http.route('/web/export/xlsx', type='http', auth="user")
    def index(self, data):
        print(aws_access_key_id)
        print(bucket_s3)
        data_dict = json.loads(data)

        model_name = data_dict.get('model')
        fields = [field['name'] for field in data_dict.get('fields', [])]
        domain = data_dict.get('domain', [])
        records = request.env[model_name].sudo().search_read(domain, fields, offset=0, limit=None, order=None)

        # Tạo DataFrame từ dữ liệu truy vấn được
        df = pd.DataFrame(records)
        file_dir = 'odoo/addons_custom/web_custom/controllers'
        file_name = f'{model_name.replace(".", "_")}.csv'
        file_path = os.path.join(file_dir, file_name)

        os.makedirs(file_dir, exist_ok=True)
        df.to_csv(file_path, index=False)

        # Upload file lên S3
        bucket_name = bucket_s3
        response = upload_file_to_s3(file_path, bucket_name, file_name)
        try:
            return super(CustomExcelExport, self).base(data)
        except Exception as exc:
            _logger.exception("Exception during request handling.")
            payload = json.dumps({
                'code': 200,
                'message': "Odoo Server Error",
                'data': http.serialize_exception(exc)
            })
            raise InternalServerError(payload) from exc