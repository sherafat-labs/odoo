# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo import fields
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class TestDentalCore(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.patient = cls.env['dental.patient'].create({
            'name': 'John Doe',
            'phone': '123456789',
            'email': 'john.doe@example.com',
            'gender': 'male',
            'blood_group': 'o_pos',
        })
        cls.dentist = cls.env['dental.dentist'].create({
            'name': 'Dr. Smith',
            'license_number': 'DEN12345',
            'specialization': 'general',
        })
        cls.treatment = cls.env['dental.treatment'].create({
            'name': 'Teeth Cleaning',
            'code': 'TC01',
            'duration': 1.0,
            'cost': 100.0,
        })

    def test_01_create_patient_and_dentist(self):
        self.assertEqual(self.patient.name, 'John Doe')
        self.assertEqual(self.patient.blood_group, 'o_pos')
        self.assertEqual(self.dentist.license_number, 'DEN12345')

    def test_02_create_appointment_and_workflow(self):
        appointment = self.env['dental.appointment'].create({
            'patient_id': self.patient.id,
            'dentist_id': self.dentist.id,
            'treatment_ids': [(4, self.treatment.id)],
            'appointment_date': fields.Datetime.now(),
        })
        self.assertEqual(appointment.state, 'draft')
        self.assertEqual(appointment.duration, 1.0)

        appointment.action_confirm()
        self.assertEqual(appointment.state, 'confirmed')

        appointment.action_start()
        self.assertEqual(appointment.state, 'in_progress')

        appointment.action_done()
        self.assertEqual(appointment.state, 'done')

    def test_03_patient_appointment_count(self):
        self.assertEqual(self.patient.appointment_count, 0)
        self.env['dental.appointment'].create({
            'patient_id': self.patient.id,
            'dentist_id': self.dentist.id,
            'appointment_date': fields.Datetime.now(),
        })
        self.assertEqual(self.patient.appointment_count, 1)
