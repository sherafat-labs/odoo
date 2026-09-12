# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta


class DentalAppointment(models.Model):
    _name = 'dental.appointment'
    _description = 'Dental Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'appointment_date desc'

    name = fields.Char(string='Appointment Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('dental.patient', string='Patient', required=True, tracking=True)
    dentist_id = fields.Many2one('dental.dentist', string='Dentist', required=True, tracking=True)
    treatment_ids = fields.Many2many('dental.treatment', string='Treatments')
    appointment_date = fields.Datetime(string='Date & Time', required=True, default=fields.Datetime.now, tracking=True)
    duration = fields.Float(string='Duration (Hours)', default=0.5, compute='_compute_duration', store=True, readonly=False)
    end_date = fields.Datetime(string='End Date', compute='_compute_end_date', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', required=True, tracking=True)
    notes = fields.Text(string='Notes')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('dental.appointment') or _('New')
        return super().create(vals_list)

    @api.depends('treatment_ids')
    def _compute_duration(self):
        for record in self:
            if record.treatment_ids:
                record.duration = sum(record.treatment_ids.mapped('duration'))
            elif not record.duration:
                record.duration = 0.5

    @api.depends('appointment_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if record.appointment_date and record.duration:
                record.end_date = record.appointment_date + timedelta(hours=record.duration)
            else:
                record.end_date = record.appointment_date

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_start(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})
