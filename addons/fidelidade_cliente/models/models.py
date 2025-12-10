# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fidelidade_cliente(models.Model):
    _inherit = 'res.partner'
    codigo_socio = fields.Char(string = "codigo_socio")
    nivel_fidelidad = fields.Char(string = "nivel_fidelidad", compute = "nivel_felicidad_calculo")

    @api.depends('codigo_socio')
    def nivel_felicidad_calculo(self):
        for record in self:
            if record.codigo_socio:
                if record.codigo_socio.startswith("G"):
                    record.nivel_fidelidad = "Gold"
                else:
                    record.nivel_fidelidad = "Premium"
            else:
                record.nivel_fidelidad = "Standard"

