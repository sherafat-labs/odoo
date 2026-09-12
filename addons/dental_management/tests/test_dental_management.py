# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo import fields


class TestDentalManagement(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.patient = cls.env['dental.patient'].create({
            'name': 'Jane Doe',
            'phone': '987654321',
        })
        cls.dentist = cls.env['dental.dentist'].create({
            'name': 'Dr. Johnson',
            'license_number': 'DEN67890',
        })
        cls.chair = cls.env['dental.chair'].create({
            'name': 'Chair 1',
            'code': 'CH01',
            'location': 'Room A',
        })
        cls.appointment = cls.env['dental.appointment'].create({
            'patient_id': cls.patient.id,
            'dentist_id': cls.dentist.id,
            'chair_id': cls.chair.id,
            'appointment_date': fields.Datetime.now(),
        })

    def test_01_chair_assignment(self):
        self.assertEqual(self.appointment.chair_id.name, 'Chair 1')
        self.assertEqual(self.appointment.chair_id.location, 'Room A')

    def test_02_tooth_record(self):
        tooth_rec = self.env['dental.tooth.record'].create({
            'patient_id': self.patient.id,
            'appointment_id': self.appointment.id,
            'tooth_number': '11',
            'condition': 'decayed',
            'notes': 'Upper right central incisor cavity',
        })
        self.assertEqual(tooth_rec.tooth_number, '11')
        self.assertEqual(tooth_rec.condition, 'decayed')
        self.assertIn(tooth_rec, self.appointment.tooth_record_ids)

    def test_03_prescription(self):
        prescription = self.env['dental.prescription'].create({
            'patient_id': self.patient.id,
            'dentist_id': self.dentist.id,
            'appointment_id': self.appointment.id,
            'line_ids': [
                (0, 0, {
                    'medicine_name': 'Amoxicillin',
                    'dosage': '500mg',
                    'frequency': '3 times daily',
                    'duration_days': 7,
                }),
                (0, 0, {
                    'medicine_name': 'Ibuprofen',
                    'dosage': '400mg',
                    'frequency': 'As needed for pain',
                    'duration_days': 5,
                })
            ]
        })
        self.assertEqual(len(prescription.line_ids), 2)
        self.assertIn(prescription, self.appointment.prescription_ids)
