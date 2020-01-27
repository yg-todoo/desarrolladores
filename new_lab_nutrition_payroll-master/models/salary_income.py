# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SalaryIncome(models.Model):
	_name = 'newlabnutrition.payroll.salary.income'
	
	name = fields.Char(string='Descripción', required=True)
	code = fields.Char(string='Código', required=True, help="The code that can be used in the salary rules")
	number_of_hours = fields.Float(string='Número de horas')
	number_of_days = fields.Float(string='Número de días')
	value = fields.Float(string='Valor')

class OverTime(models.Model):
	_inherit = 'newlabnutrition.payroll.salary.income'
	
	_name = 'newlabnutrition.payroll.overtime'


class VacationsDays(models.Model):
	_inherit = 'newlabnutrition.payroll.salary.income'
	
	_name = 'newlabnutrition.payroll.vacations.days'
	
class IncapacityDays(models.Model):
	_inherit = 'newlabnutrition.payroll.salary.income'
	
	_name = 'newlabnutrition.payroll.incapacity.days'


class LicenseDays(models.Model):
	_inherit = 'newlabnutrition.payroll.salary.income'
	
	_name = 'newlabnutrition.payroll.license.days'