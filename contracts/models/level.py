from odoo import api, fields, models, tools, _

class Level(models.Model):
    _name = 'level'
    _description = 'Level'

    name = fields.Char(string="Level Name", required=True)
    code = fields.Char(string="Level Code", required=True)
