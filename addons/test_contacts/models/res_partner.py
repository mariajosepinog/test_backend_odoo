
from odoo import fields, models, api, exceptions

class ResPartner(models.Model):
    _inherit = 'res.partner'

#Parte de los requerimientos de los campos se piden 2 tipo float y 1 tipo selection
    x_coordinate = fields.Float('')
    y_coordinate = fields.Float('')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ]
    )