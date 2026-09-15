# -*- coding: utf-8 -*-
{
    'name': 'Dental Management Extension',
    'version': '18.0.1.0.0',
    'category': 'Healthcare/Dental',
    'summary': 'Advanced clinic management: Tooth Records (FDI), Chairs/Rooms, and Prescriptions',
    'description': """
Dental Management Extension Module
==================================
- Clinic Chairs and Treatment Room allocation.
- Dental Charting & FDI Tooth Record tracking per patient.
- Dental Prescriptions & Dosage management linked to appointments.
    """,
    'author': 'Odoo S.A.',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'depends': ['dental_core'],
    'data': [
        'security/dental_management_security.xml',
        'security/ir.model.access.csv',
        'data/dental_management_sequence_data.xml',
        'views/dental_chair_views.xml',
        'views/dental_tooth_record_views.xml',
        'views/dental_prescription_views.xml',
        'views/dental_appointment_extension_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
