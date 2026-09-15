# -*- coding: utf-8 -*-
{
    'name': 'Dental Core Management',
    'version': '18.0.1.0.0',
    'category': 'Healthcare/Dental',
    'summary': 'Core module to manage dentist clinic appointments, patients, dentists, and treatments',
    'description': """
Dental Core Management Module
=============================
- Patient management with medical background and dental history.
- Dentist / Practitioner profile management.
- Dental Treatment catalog with standard costs and durations.
- Appointment scheduling and workflow state tracking.
    """,
    'author': 'Odoo S.A.',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'calendar'],
    'data': [
        'security/dental_security.xml',
        'security/ir.model.access.csv',
        'data/dental_sequence_data.xml',
        'views/dental_appointment_views.xml',
        'views/dental_patient_views.xml',
        'views/dental_dentist_views.xml',
        'views/dental_treatment_views.xml',
        'views/dental_menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
