# -*- coding: utf-8 -*-

 from odoo import models, fields


 class deportes(models.Model):
     _name = 'deportes.nombres'
     _description = 'Esta clase almacena los nombres de los deportes'

     nombre = fields.Char()
     ID deporte = fields.Integer()
     valoracion = fields.Float(compute="_value_pc", store=True)
     descripcion = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
