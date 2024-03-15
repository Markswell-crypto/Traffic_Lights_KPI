# -*- coding: utf-8 -*-

{
    'name': "Trafic Lights KPI - HR Dashboard",
    'version': '16.0.1.0.1',
    'summary': """Trafic Lights KPI - HR Dashboard""",
    'description': """Trafic Lights KPI - HR Dashboard""",
    'category': 'Generic Modules/Human Resources',
    'author': 'Smoothtel & Data Solutions',
    'company': 'Smoothtel & Data Solutions',
    'maintainer': 'Smoothtel & Data Solutions',
    'website': "https://www.openhrms.com",
    'depends': ['hr', 'hr_holidays', 'hr_timesheet', 'hr_payroll_community',
                'hr_attendance', 'hr_timesheet_attendance',
                'hr_recruitment', 'hr_resignation', 'event',
                'hr_reward_warning', 'base'],
    
    'data': [
        'security/ir.model.access.csv',
        'report/broadfactor.xml',
        'views/dashboard_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hrms_dashboard/static/src/css/hrms_dashboard.css',
            'hrms_dashboard/static/src/css/lib/nv.d3.css',
            'hrms_dashboard/static/src/js/hrms_dashboard.js',
            'hrms_dashboard/static/src/js/lib/d3.min.js',
            'hrms_dashboard/static/src/xml/hrms_dashboard.xml',
        ],
    },

    'images': ["static/description/banner.png"],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
