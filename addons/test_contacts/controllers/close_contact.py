# from odoo import http
# from odoo.http import request
# from odoo.exceptions import ValidationError

# class ContactController(http.Controller):
#     @http.route('/contact/close_contact', type='json', auth="public", methods=['GET'], website=True, csfr=False)
#     def get_close_contacts(self, x_coordinate=None, y_coordinate=None, max_distance=None, gender=None,**kwargs):
#         try:
#             # Validar que los parámetros obligatorios estén presentes
#             if not all([x_coordinate, y_coordinate, max_distance]):
#                 raise ValidationError("Los parámetros 'x_coordinate', 'y_coordinate' y 'max_distance' son obligatorios.")
            
#             contacts = request.env['res.partner'].search([])

#             # Filtrar contactos por género si se proporciona
#             if gender:
#                 contacts = contacts.filtered(lambda c: c.gender == gender)

#             contact_list = []
#             for contact in contacts:
#                 distance = ((contact.x_coordinate - x_coordinate) ** 2 + (contact.y_coordinate - y_coordinate) ** 2) ** 0.5
#                 if distance <= max_distance:
#                     contact_list.append({
#                         'name': contact.name,
#                         'distance': distance
#                     })

#                 return {
#                     'success': True,
#                     'error': None,
#                     'data': contact_list
#                 }

#         except ValidationError as e:
#             return {
#                 'success': False,
#                 'error': str(e),
#                 'data': []
#         }
            