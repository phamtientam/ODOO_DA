from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta

class ContractEnterprise(models.Model):
    _name = "contract.enterprise"
    _description = "contract enterprise model"

    def _default_sign_date(self):
        next_week = fields.Datetime.now() + timedelta(weeks=1)
        if next_week.weekday() >= 5:
            next_week += timedelta(days=7 - next_week.weekday())
        return next_week

    id = fields.Integer('id', required=True)
    name = fields.Char("contract name", required=True)
    start_date = fields.Datetime('start date', required=True, select=True, default=datetime.now())
    end_date = fields.Datetime('end date', required=True, select=True)
    type_contract = fields.Integer('contract type', required=True)
    sign_date = fields.Datetime('sign date', required=True, select=True, default=_default_sign_date)
    salary_level = fields.Float('salary level', required=False, default=0)
    effective_salary = fields.Float('effective salary', required=False, default=0)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True, ondelete='cascade')
    # role_name = fields.Char(compute='_compute_get_job_name', store=True, string='Role Name', readonly=False)
    # level_name = fields.Char(compute='_compute_get_job_name', store=True, string='Level Name', readonly=False)
    # job_name = fields.Char(compute='_compute_get_job_name', store=True, string='Job Name', readonly=False)
    '''
        ondelete : có 4 type
            + cascade : khi một bản ghi được xóa, tất cả các bản ghi liên quan trong table con sẽ cũng được xóa.
            + set null :  khi một bản ghi được xóa, trường Many2one sẽ được đặt thành giá trị NULL.
            + restrict : Odoo sẽ không cho phép xóa bản ghi nếu có bản ghi liên quan trong bảng con.
            + no action : Odoo sẽ không thực hiện bất kỳ hành động nào khi một bản ghi được xóa. Bạn phải quản lý các hành động liên quan bằng cách thủ công
    '''
    sign_day = fields.Date(string="Sign Date")
    status = fields.Selection([
                ('new', 'New'),
                ('running', 'Running'),
                ('expired', 'Expired'),
                ('pause', 'Pause')
            ], string='Status', default='new')

    total_salary = fields.Float(string='Total Salary', compute='_compute_total_salary', store=True)

    @api.depends('salary_level', 'effective_salary')
    def _compute_total_salary(self):
        for record in self:
            record.total_salary = record.salary_level + record.effective_salary

    # @api.depends('employee_id')
    # def _compute_get_job_name(self):
    #     for record in self:
    #         if record:
    #             if record.employee_id.work_experiences_ids:
    #                 # record.role_name = record.employee_id.work_experiences_ids.role_id.name
    #                 print(record.employee_id.work_experiences_ids.job_id.name)
    #                 print(record.employee_id.work_experiences_ids.role_id.name)
    #                 print(record.employee_id.work_experiences_ids.level_id.name)
                    # record.job_name = record.employee_id.work_experiences_ids.job_id.name
                    # record.level_name = record.employee_id.work_experiences_ids.level_id.name


    '''
    compute và related
    compute : được sử dụng để tính toán giá trị dựa trên các trường khác trong cùng một bảng hoặc từ các bảng khác
    related : được sử dụng để truy xuất và hiển thị giá trị của một trường từ một bảng khác mà đã có quan hệ với bảng hiện tại
    '''
