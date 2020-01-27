# -*- coding: utf-8 -*-
from odoo import http

# class NewLabNutritionPayroll(http.Controller):
#     @http.route('/newlabnutrition_payroll/newlabnutrition_payroll/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/newlabnutrition_payroll/newlabnutrition_payroll/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('newlabnutrition_payroll.listing', {
#             'root': '/newlabnutrition_payroll/newlabnutrition_payroll',
#             'objects': http.request.env['newlabnutrition_payroll.newlabnutrition_payroll'].search([]),
#         })

#     @http.route('/newlabnutrition_payroll/newlabnutrition_payroll/objects/<model("newlabnutrition_payroll.newlabnutrition_payroll"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('newlabnutrition_payroll.object', {
#             'object': obj
#         })