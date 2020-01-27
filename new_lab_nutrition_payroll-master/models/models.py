# -*- coding: utf-8 -*-

from odoo import models, fields, api


# 								inherit 'hr.contract'
class HrContract(models.Model):
	_inherit = 'hr.contract'
	
	# Add fields
	smmlv = fields.Integer(string="Valor", default=828116, readonly=True,
						   help="Salario Mínimo 2019 Mensual en Colombia")
	
	EPS = fields.Many2one('newlabnutrition.payroll.eps', string='Nombre', required=True)
	pension = fields.Many2one('newlabnutrition.payroll.pension', string='Nombre', required=True)
	cesantia = fields.Many2one('newlabnutrition.payroll.cesantia', string='Nombre', required=True)
	

# 								inherit 'hr.employee'
class HrEmployee(models.Model):
	_inherit = 'hr.employee'
	
	# Mod attributes
	country_id = fields.Many2one(default=lambda self:  self.env['res.country'].search([('name', '=', 'Colombia')]))
	country_of_birth = fields.Many2one(default=lambda self:  self.env['res.country'].search([('name', '=', 'Colombia')]))
	certificate = fields.Selection([
		('incomplete_bachelor', 'Bachiller Académico incompleto'),
		('academic_bachelor', 'Bachiller Académico'),
		('technical_bachelor', 'Bachiller Técnico'),
		('graduate', 'Pregrado/Universitario'),
		('specialization', 'Especialización'),
		('master', 'Maestría'),
		('doctorate', 'Doctorado'),
		('post_doctorate', 'PostDoctorado'),
		('other', 'Otro')
	], 'Certificate Level', default='academic_bachelor', groups="hr.group_hr_user")
	# Add fields
	work_mobile_phone = fields.Char('Celular N°')
	documento_type = fields.Selection([
		('CC', 'Cédula de ciudadanía'),
		('CE', 'Cédula de extranjería'),
		('passport', 'Pasaporte'),
		('TI', 'Tarjeta de identidad'),
		('RC', 'Registro civil'),
		('PEP', 'Permiso especial de permanencia'),
		('other', 'Otro')], string="Tipo de documento", default='CC', groups="hr.group_hr_user")
	document_type_name = fields.Char('Nombre del Tipo de documento', groups="hr.group_hr_user")
	expedition_place = fields.Char(string='Lugar de expedición', required=True, groups="hr.group_hr_user")
	personal_number = fields.Integer(string="Télefono fijo N°", groups="hr.group_hr_user")
	personal_email = fields.Char(string="E-mail", groups="hr.group_hr_user")
	personal_address = fields.Char(string="Dirección de residencia", groups="hr.group_hr_user")
	rh = fields.Char(string='RH')
	father_name = fields.Char(string="Nombres y Apellidos")
	father_address = fields.Char(string="Dirección", groups="hr.group_hr_user")
	father_phone_number = fields.Integer(string="Celular N°", groups="hr.group_hr_user")
	mother_name = fields.Char(string="Nombres y Apellidos")
	mother_address = fields.Char(string="Dirección", groups="hr.group_hr_user")
	mother_phone_number = fields.Integer(string="Celular N°", groups="hr.group_hr_user")
	son_name_1 = fields.Char(string="Nombres y Apellidos")
	son_name_2 = fields.Char(string="Nombres y Apellidos")
	son_name_3 = fields.Char(string="Nombres y Apellidos")
	son_name_4 = fields.Char(string="Nombres y Apellidos")
	son_name_5 = fields.Char(string="Nombres y Apellidos")
	son_name_6 = fields.Char(string="Nombres y Apellidos")
	# Partner
	eps = fields.Many2one('res.partner', string="EPS")
	pension = fields.Many2one('res.partner', string="Fondo de Pensiones")
	cesantias = fields.Many2one('res.partner', string="Fondo de Cesantías")
	arl = fields.Many2one('res.partner', string="Aseguradora de Riesgos Laborales")
	ccj = fields.Many2one('res.partner', string="Caja de Compensación")
	lv_arl = fields.Selection(
		[('lv_1', 'Clase de Riesgo 1'),
		('lv_2', 'Clase de Riesgo 2'),
		('lv_3', 'Clase de Riesgo 3'),
		('lv_4', 'Clase de Riesgo 4'),
		('lv_5', 'Clase de Riesgo 5')], string="ARL - Clases de Riesgo", groups="hr.group_hr_user", default='lv_1')
	
# 								inherit 'hr.payslip'
class HrPayslip(models.Model):
	_inherit = 'hr.payslip'
	
	overtime_line_ids = fields.Many2many('newlabnutrition.payroll.overtime',
										 string='Lista de Horas extra, ordinarias y recargos')
	vacations_days_line_ids = fields.Many2many('newlabnutrition.payroll.vacations.days',
											   string='Lista de Tipos de Vacaciones')
	incapacity_days_line_ids = fields.Many2many('newlabnutrition.payroll.incapacity.days',
												string='Lista de Tipos de Incapacidad')
	license_days_line_ids = fields.Many2many('newlabnutrition.payroll.license.days',
												string='Lista de Tipos de Licencia')
	salary_income_line_ids = fields.Many2many('newlabnutrition.payroll.salary.income',
											 string='Lista de Ingresos adicionales')
	non_salary_income_line_ids = fields.Many2many('newlabnutrition.payroll.non.salary.income',
											  string='Lista de Ingresos adicionales')
	deductions_line_ids = fields.Many2many('newlabnutrition.payroll.deductions',
												  string='Lista de Ingresos adicionales')
