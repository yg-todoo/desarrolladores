# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Deductions(models.Model):
	_inherit = 'newlabnutrition.payroll.salary.income'
	
	_name = 'newlabnutrition.payroll.deductions'