# -*- coding: utf-8 -*-
{
    'name': "zxc Education Student",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "minh",
    'website': "https://facebook/minhtran0202",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/education_student_views.xml',
        'views/student_level_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],x
    'installable': True,
    'application': True,
}