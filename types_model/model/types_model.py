from odoo import api, fields, models, tools, _

class PersonInfo(models.AbstractModel):
    _name = "person.info"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    address = fields.Char(string="Address")

class ActionInfo(models.TransientModel):
    _name = 'action.info'
    _description = 'Action Info'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    address = fields.Char(string='Address')
    email = fields.Char(string='Email')
    company = fields.Char(string='Company')
    phone = fields.Char(string='Phone Number')
    enterprise = fields.Char(string='Enterprise')

    def save_contact_info(self):
        print("Contact Information:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
        print("Email:", self.email)
        print("Company:", self.company)
        print("Phone Number:", self.phone)
        print("Enterprise:", self.enterprise)


class EmployeeInfo(models.Model):
    _name = 'employee.info'
    _inherit = 'person.info'
    _description = 'Employee'

    email = fields.Char(string='Email', required=True)
    company = fields.Char(string="Company", required=True)

class CustomerInfo(models.Model):
    _name = 'customer.info'
    _inherit = 'person.info'
    _description = 'Customer'

    phone = fields.Char(string="Phone Number", required=True)
    enterprise = fields.Char(string="Enterprise", required=True)
