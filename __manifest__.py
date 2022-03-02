# -*- coding: utf-8 -*-
{
    'name': "odoo_x",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/empresa_report.xml',
        'report/locales_report.xml',
        'report/empleados_report.xml',
        'report/clientes_report.xml',
        'report/pagos_report.xml',
        'report/cesta_report.xml',
        'report/ordenadores_report.xml',
        'report/ratones_report.xml',
        'report/moviles_report.xml',
        'report/cables_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
