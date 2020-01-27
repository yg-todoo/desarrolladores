# -*- coding: utf-8 -*-
{
    'name': "Módulo de Nómina - NewLab Nutrition",



    'description': """
    Módulo de Nómina
    ================
    """,

    'author': "New Lab Nutrition",
    'website': "http://newlabnutrition.com",
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'hr_payroll',
        'contacts',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract_views.xml',
        'views/hr_employee_views.xml',
        'views/entities_views.xml',
        'views/salary_income_views.xml',
        'views/non_salary_income_views.xml',
        'views/deductions_views.xml',
        'views/hr_payslip_views.xml'
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}