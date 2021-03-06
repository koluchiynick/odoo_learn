# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/openacademy_groups.xml',
        'security/course_security.xml',
        'security/ir.model.access.csv',
        'wizard/create_attendees_view.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/partner_views.xml',
        'views/dashboard_view.xml',
        'views/openacademy_menus.xml',
        'report/session_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/course_demo.xml',
    ],
}
