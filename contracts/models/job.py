from odoo import api, fields, models, tools, _

class Job(models.Model):
    _name = 'job'
    _description = 'Job'

    name = fields.Char(string="Job Name", required=True)
    code = fields.Char(string="Job Code", required=True)
