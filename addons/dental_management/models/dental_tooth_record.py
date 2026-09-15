# -*- coding: utf-8 -*-

from odoo import models, fields


class DentalToothRecord(models.Model):
    _name = 'dental.tooth.record'
    _description = 'Patient Tooth Record (FDI Charting)'

    patient_id = fields.Many2one('dental.patient', string='Patient', required=True, ondelete='cascade')
    appointment_id = fields.Many2one('dental.appointment', string='Appointment')
    tooth_number = fields.Selection([
        # Upper Right Quadrant (11-18)
        ('11', '11 - Central Incisor (UR)'),
        ('12', '12 - Lateral Incisor (UR)'),
        ('13', '13 - Canine (UR)'),
        ('14', '14 - First Premolar (UR)'),
        ('15', '15 - Second Premolar (UR)'),
        ('16', '16 - First Molar (UR)'),
        ('17', '17 - Second Molar (UR)'),
        ('18', '18 - Third Molar / Wisdom (UR)'),
        # Upper Left Quadrant (21-28)
        ('21', '21 - Central Incisor (UL)'),
        ('22', '22 - Lateral Incisor (UL)'),
        ('23', '23 - Canine (UL)'),
        ('24', '24 - First Premolar (UL)'),
        ('25', '25 - Second Premolar (UL)'),
        ('26', '26 - First Molar (UL)'),
        ('27', '27 - Second Molar (UL)'),
        ('28', '28 - Third Molar / Wisdom (UL)'),
        # Lower Left Quadrant (31-38)
        ('31', '31 - Central Incisor (LL)'),
        ('32', '32 - Lateral Incisor (LL)'),
        ('33', '33 - Canine (LL)'),
        ('34', '34 - First Premolar (LL)'),
        ('35', '35 - Second Premolar (LL)'),
        ('36', '36 - First Molar (LL)'),
        ('37', '37 - Second Molar (LL)'),
        ('38', '38 - Third Molar / Wisdom (LL)'),
        # Lower Right Quadrant (41-48)
        ('41', '41 - Central Incisor (LR)'),
        ('42', '42 - Lateral Incisor (LR)'),
        ('43', '43 - Canine (LR)'),
        ('44', '44 - First Premolar (LR)'),
        ('45', '45 - Second Premolar (LR)'),
        ('46', '46 - First Molar (LR)'),
        ('47', '47 - Second Molar (LR)'),
        ('48', '48 - Third Molar / Wisdom (LR)'),
    ], string='Tooth Number (FDI)', required=True)
    condition = fields.Selection([
        ('healthy', 'Healthy'),
        ('decayed', 'Decayed / Caries'),
        ('filled', 'Filled'),
        ('missing', 'Missing'),
        ('extracted', 'Extracted'),
        ('crown', 'Crown / Bridge'),
        ('implanted', 'Implanted'),
        ('root_canal', 'Root Canal Treated')
    ], string='Condition', default='healthy', required=True)
    notes = fields.Text(string='Notes & Treatment Plan')
    treatment_id = fields.Many2one('dental.treatment', string='Associated Treatment')
