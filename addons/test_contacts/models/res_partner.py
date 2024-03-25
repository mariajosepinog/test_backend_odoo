from odoo import fields, models

# En este archivo se define el modelo a utilizar.
# Como se puede ver, consiste en la herencia del modelo res.partner
# al que se le añaden 3 atributos:
# - x_coordinate e y_coordinate corresponden a atributos de tipo Flotante
# - gender corresponde a un atributo de tipo Selection, con las opciones male, female y other
class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_coordinate = fields.Float(string='X Coordinate')
    y_coordinate = fields.Float(string='Y Coordinate')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')