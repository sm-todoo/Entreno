# -*- coding: utf-8 -*-
# from odoo import http


# class Mod1(http.Controller):
#     @http.route('/mod1/mod1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mod1/mod1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mod1.listing', {
#             'root': '/mod1/mod1',
#             'objects': http.request.env['mod1.mod1'].search([]),
#         })

#     @http.route('/mod1/mod1/objects/<model("mod1.mod1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mod1.object', {
#             'object': obj
#         })
