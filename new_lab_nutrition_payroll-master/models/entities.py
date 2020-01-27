# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entities(models.Model):
    _name = 'newlabnutrition.payroll.entities'
    
    name = fields.Char(string='Nombre', required=True)
    start_date = fields.Date(default=fields.Date.today, string='Fecha de Inicio')
    phone_number = fields.Integer(string='N° Télefono')
    email = fields.Char(string='E-mail')
    commercial_entity = fields.Boolean(string='Entidad Comercial')

class EPS(models.Model):
    _inherit = 'newlabnutrition.payroll.entities'
    
    _name = 'newlabnutrition.payroll.eps'
    

class Pension(models.Model):
    _inherit = 'newlabnutrition.payroll.entities'
    
    _name = 'newlabnutrition.payroll.pension'
    

class Cesantia(models.Model):
    _inherit = 'newlabnutrition.payroll.entities'
    
    _name = 'newlabnutrition.payroll.cesantia'