# -*- coding: utf-8 -*-
{
    'name': "My pet - minh",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "minh",
    'website': "https://facebook.com",
    'category': 'Uncategorized',
    'version': '1',
    'depends': [
        'product',
    ],
    'data': [
        # 'data/data.xml',
        'security/ir.model.access.csv',
        'security/my_pet_security.xml',
        'views/my_pet_views.xml',
        'views/my_pet_plus_views.xml',
        'wizard/batch_update.xml',
        'views/product_pet_view.xml',
        'views/templates.xml',
        'views/my_pet_view_new.xml'
    ],
    'qweb': [
        'static/src/xml/btn_tree_multi_update.xml',
        ],
    'installable': True,
    'application': True,
}