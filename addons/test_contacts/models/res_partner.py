
from odoo import fields, models, api, exceptions

class ResPartner(models.Model):
    _inherit = 'res.partner'
    # Aqui debajo se declaran las variables solicitadas para agregar al modelo

    # DECLARACION COORDENADA X
    x_coordinate = fields.Float(string="x_coordinate")

    # DECLARACION COORDENADA X
    y_coordinate = fields.Float(String="y_coordinate")

    # DECLARACION COORDENADA X
    gender = fields.Selection([('male','male'),('female','female'),("other","other")])