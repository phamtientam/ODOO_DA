# -*- coding: utf-8 -*-

{
    'name': 'HR Employee Custom',
    'category': 'Website/Website',
    'summary': 'hr_employee models',
    'version': '1.0',
    'author': 'Pham tien tam',
    'description': """
        This is a module Hr Employee
    """,
    'depends': ['hr', 'contracts'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml'
    ],
    'installable': True,
    'application': True,
}
