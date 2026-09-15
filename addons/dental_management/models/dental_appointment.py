# -*- coding: utf-8 -*-

from odoo import models, fields


class DentalAppointment(models.Model):
    _inherit = 'dental.appointment'

    chair_id = fields.Many2one('dental.chair', string='Dental Chair / Room')
    tooth_record_ids = fields.One2many('dental.tooth.record', 'appointment_id', string='Tooth Chart Records')
    prescription_ids = fields.One2many('dental.prescription', 'appointment_id', string='Prescriptions')
