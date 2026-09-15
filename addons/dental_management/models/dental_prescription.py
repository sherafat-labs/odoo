# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class DentalPrescription(models.Model):
    _name = 'dental.prescription'
    _description = 'Dental Prescription'

    name = fields.Char(string='Prescription Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('dental.patient', string='Patient', required=True)
    dentist_id = fields.Many2one('dental.dentist', string='Dentist', required=True)
    appointment_id = fields.Many2one('dental.appointment', string='Appointment')
    date = fields.Date(string='Prescription Date', default=fields.Date.context_today, required=True)
    line_ids = fields.One2many('dental.prescription.line', 'prescription_id', string='Prescription Lines')
    notes = fields.Text(string='Instructions / Notes')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('dental.prescription') or _('New')
        return super().create(vals_list)


class DentalPrescriptionLine(models.Model):
    _name = 'dental.prescription.line'
    _description = 'Dental Prescription Line'

    prescription_id = fields.Many2one('dental.prescription', string='Prescription', required=True, ondelete='cascade')
    medicine_name = fields.Char(string='Medicine Name', required=True)
    dosage = fields.Char(string='Dosage (e.g. 500mg)', required=True)
    frequency = fields.Char(string='Frequency (e.g. 3 times daily)', required=True)
    duration_days = fields.Integer(string='Duration (Days)', default=5)
    instructions = fields.Char(string='Special Instructions')
