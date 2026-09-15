# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DentalDentist(models.Model):
    _name = 'dental.dentist'
    _description = 'Dental Practitioner'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    partner_id = fields.Many2one(
        'res.partner', string='Contact', required=True, ondelete='cascade', delegate=True
    )
    license_number = fields.Char(string='License Number', required=True)
    specialization = fields.Selection([
        ('general', 'General Dentistry'),
        ('orthodontics', 'Orthodontics'),
        ('periodontics', 'Periodontics'),
        ('endodontics', 'Endodontics'),
        ('pediatric', 'Pediatric Dentistry'),
        ('prosthodontics', 'Prosthodontics'),
        ('surgery', 'Oral & Maxillofacial Surgery')
    ], string='Specialization', default='general', required=True)
    active = fields.Boolean(string='Active', default=True)
    appointment_ids = fields.One2many('dental.appointment', 'dentist_id', string='Appointments')
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment_ids)
