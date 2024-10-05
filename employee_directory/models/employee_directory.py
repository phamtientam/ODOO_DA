from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta

class EmployeeDirectory(models.Model):
    _name = 'employee.directory'
    _description = 'Employee Directory'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    address = fields.Char(string='Address', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number')
    contract_count = fields.Integer(string="Contract Count", compute='_compute_contract_count')

    # action này thực hiện mở 1 cửa sổ mới hiển thị tất cả contracts của employee
    def action_open_contracts(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Contracts',
            'res_model': 'contract.enterprise',
            'domain': [('employee_id', '=', self.id)], # employee_id của table contract trùng với id của employee
            'view_mode': 'tree,form',
            'target': 'new', # thiết lập để cửa sổ mới mở ra trong chính trình duyệt hiện tại, ngoài ra bao gồm : new, inline, fullscreen, popup
        }

    def _compute_contract_count(self):
        # đối với case chắc chắn chỉ get ra 1 record cụ thể thì có thể dùng trực tiếp biến self để truy vấn
        # sử dụng rec sẽ an toàn hơn cho những case không biết rõ sẽ có bao nhiêu records
        for rec in self:
            contract_count = self.env['contract.enterprise'].search_count([('employee_id', '=', rec.id)])
            rec.contract_count = contract_count