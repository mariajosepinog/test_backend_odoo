from odoo import fields, models, api, exceptions

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # 1. Campo x_coordinate (coordenada X)
    x_coordinate = fields.Float(string="Coordenada X")

    # 2. Campo y_coordinate (coordenada Y)
    y_coordinate = fields.Float(string="Coordenada Y")

    # 3. Campo gender (género)
    gender = fields.Selection(
        string="Género",
        selection=[
            ('male', 'Hombre'),
            ('female', 'Mujer'),
            ('other', 'Otro'),
        ],
        default='male',
    )

    #Restricciones
    @api.constrains('x_coordinate', 'y_coordinate')
    def _validate_coordinates(self):
        for record in self:
            if not isinstance(record.x_coordinate, float):
                raise exceptions.ValidationError("La coordenada X debe ser un número decimal.")
            if not isinstance(record.y_coordinate, float):
                raise exceptions.ValidationError("La coordenada Y debe ser un número decimal.")
