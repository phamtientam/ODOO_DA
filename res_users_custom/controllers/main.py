from odoo import http
from odoo.http import request
from odoo.tools import json


class UsersController(http.Controller):
    @http.route('/api/users', type='http', auth='user')
    def get_users(self):
        users = request.env['res.users'].search([])
        users_info = []

        for user in users:
            users_info.append({
                'id': user.id,
                'name': user.name,
                'login': user.login,
                'email': user.email,
                'active': user.active,
            })

        return request.make_response(
            json.dumps({'status': 200, 'data': users_info}),
            headers={'Content-Type': 'application/json'}
        )

    @http.route('/api/authenticate', type='http', auth='none', methods=['GET'], csrf=False)
    def authenticate_user(self, **kwargs):
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        }

        db = 'odoo_study'
        login = kwargs.get('login')
        password = kwargs.get('password')

        uid = request.session.authenticate(db, login, password)

        if uid:
            return request.make_response({'status': 200, 'message': 'Authentication successful', 'user_id': uid},
                                         headers=headers)
        else:
            return request.make_response({'status': 401, 'message': 'Authentication failed'}, headers=headers)