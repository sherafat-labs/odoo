# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DentalPatient(models.Model):
    _name = 'dental.patient'
    _description = 'Dental Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    partner_id = fields.Many2one(
        'res.partner', string='Contact', required=True, ondelete='cascade', delegate=True
    )
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    blood_group = fields.Selection([
        ('a_pos', 'A+'),
        ('a_neg', 'A-'),
        ('b_pos', 'B+'),
        ('b_neg', 'B-'),
        ('ab_pos', 'AB+'),
        ('ab_neg', 'AB-'),
        ('o_pos', 'O+'),
        ('o_neg', 'O-')
    ], string='Blood Group')
    medical_history = fields.Text(string='Medical History')
    allergies = fields.Text(string='Allergies')
    emergency_contact = fields.Char(string='Emergency Contact Name')
    emergency_phone = fields.Char(string='Emergency Contact Phone')
    appointment_ids = fields.One2many('dental.appointment', 'patient_id', string='Appointments')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)
