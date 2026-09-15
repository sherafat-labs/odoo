# -*- coding: utf-8 -*-

from odoo import models, fields


class DentalTreatment(models.Model):
    _name = 'dental.treatment'
    _description = 'Dental Treatment Catalog'

    name = fields.Char(string='Treatment Name', required=True)
    code = fields.Char(string='Code')
    description = fields.Text(string='Description')
    duration = fields.Float(string='Duration (Hours)', default=0.5)
    cost = fields.Monetary(string='Cost', currency_field='currency_id')
    currency_id = fields.Many2one(
        'res.currency', string='Currency', default=lambda self: self.env.company.currency_id
    )
    active = fields.Boolean(string='Active', default=True)
