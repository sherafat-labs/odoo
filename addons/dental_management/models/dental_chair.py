# -*- coding: utf-8 -*-

from odoo import models, fields


class DentalChair(models.Model):
    _name = 'dental.chair'
    _description = 'Dental Chair / Treatment Room'

    name = fields.Char(string='Chair / Room Name', required=True)
    code = fields.Char(string='Code')
    location = fields.Char(string='Location / Floor')
    active = fields.Boolean(string='Active', default=True)
    description = fields.Text(string='Description')
