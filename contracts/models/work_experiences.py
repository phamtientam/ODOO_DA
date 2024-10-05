from odoo import api, fields, models, tools, _

class WorkExperiences(models.Model):
    _name = 'work.experiences'
    _description = 'Work Experiences'

    from_date = fields.Datetime(string="From")
    to_date = fields.Datetime(string="To")
    company = fields.Char(string="Name Company")
    role_id = fields.Many2one('role', string='Role', required=True)
    job_id = fields.Many2one('job', string='Job', required=True)
    level_id = fields.Many2one('level', string='Level', required=True)
    reference = fields.Text(string='Reference')
    employee_id = fields.Many2one('hr.employee', string="Employee")

