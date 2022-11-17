# -*- coding: utf-8 -*-


{
    'name': 'odoo_sheftel',
    'version': '0.0.1',
    'description': "",
    'depends': [
        'base',
        'sale'
    ],
    'data': [
        'views/sale_order_modification_views.xml',

        'report/sale_report_inherit.xml',
    ],
    'application': True,
}
