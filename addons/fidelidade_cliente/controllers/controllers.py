# -*- coding: utf-8 -*-
# from odoo import http


# class FidelidadeCliente(http.Controller):
#     @http.route('/fidelidade_cliente/fidelidade_cliente', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fidelidade_cliente/fidelidade_cliente/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fidelidade_cliente.listing', {
#             'root': '/fidelidade_cliente/fidelidade_cliente',
#             'objects': http.request.env['fidelidade_cliente.fidelidade_cliente'].search([]),
#         })

#     @http.route('/fidelidade_cliente/fidelidade_cliente/objects/<model("fidelidade_cliente.fidelidade_cliente"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fidelidade_cliente.object', {
#             'object': obj
#         })

