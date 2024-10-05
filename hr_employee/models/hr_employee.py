from odoo import api, fields, models, tools, _

class HrEmployee(models.Model):
    _name = 'hr.employee'
    _description = 'HR Employee'
    _inherit = 'hr.employee'

    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('waiting_approve', 'Waiting Approve'),
            ('approved', 'Approved'),
            ('terminated', 'Terminated'),
        ], string='Status', default='draft', readonly=True
    )

    level_id = fields.Many2one('level', string='Level')
    level_name = fields.Char(related='level_id.name', string='Level Name', store=True, related_sudo=False, readonly=False)
    department_name = fields.Char(related='department_id.name', string='Department Name', store=True, related_sudo=False, readonly=False)
    job_name = fields.Char(related='job_id.name', string='Job Name', store=True, related_sudo=False, readonly=False)

    def action_submit(self):
        self.status = "waiting_approve"

    def action_approve(self):
        self.status = 'approved'

    def action_terminate(self):
        self.status = 'terminated'

    def action_set_to_draft(self):
        self.status = 'draft'
