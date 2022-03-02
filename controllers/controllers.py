# -*- coding: utf-8 -*-
# from odoo import http


# class OdooX(http.Controller):
#     @http.route('/odoo_x/odoo_x/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_x/odoo_x/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_x.listing', {
#             'root': '/odoo_x/odoo_x',
#             'objects': http.request.env['odoo_x.odoo_x'].search([]),
#         })

#     @http.route('/odoo_x/odoo_x/objects/<model("odoo_x.odoo_x"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_x.object', {
#             'object': obj
#         })
