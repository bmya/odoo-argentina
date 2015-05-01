# -*- coding: utf-8 -*-
from openerp import fields, models, api
import re


class res_partner(models.Model):
    _inherit = 'res.partner'

    responsability_id = fields.Many2one(
        'afip.responsability', 'Resposability')
    document_type_id = fields.Many2one(
        'afip.document_type', 'Document type',)
    document_number = fields.Char(
        'Document number', size=64,)
    iibb = fields.Char('Gross Income', size=64)
    start_date = fields.Date('Start-up Date')

    @api.onchange('document_number', 'document_type_id')
    def onchange_document(self):
        mod_obj = self.env['ir.model.data']
        if self.document_number and ('afip.document_type', self.document_type_id.id) == mod_obj.get_object_reference('l10n_ar_invoice', 'dt_CUIT'):
            document_number = re.sub('[^1234567890]', '', str(self.document_number))
            self.vat = 'AR%s' % document_number
            self.document_number = document_number
