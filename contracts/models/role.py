from odoo import api, fields, models, tools, _

class Role(models.Model):
    _name = 'role'
    _description = 'Role'

    name = fields.Char(string="Role Name", required=True)
    code = fields.Char(string="Role Code", required=True)
