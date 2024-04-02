from math import sqrt
from odoo import fields, models, api, exceptions, _
from odoo.http import request

class ContactAPI:
    _name = 'contact.api'

    @api.route('/contact/close_contact', methods=['GET'], auth='public')
    def get_close_contacts(self, x_coordinate, y_coordinate, max_distance, gender=None):
        """
        API REST para obtener contactos cercanos.

        Parámetros:
            x_coordinate: Coordenada X del punto de referencia.
            y_coordinate: Coordenada Y del punto de referencia.
            max_distance: Distancia máxima en kilómetros.
            gender: Género opcional para filtrar los contactos.

        Retorno:
            JSON con información de los contactos cercanos.
        Ejemplo: 
            http://localhost:8069/contact/close_contact?x_coordinate={{x_coordinate}}&y_coordinate={{y_coordinate}}&max_distance={{max_distance}}&gender={{gender}}

        """
        try:
            # Validar parámetros
            if not all(isinstance(param, (float, int)) for param in [x_coordinate, y_coordinate, max_distance]):
                raise ValueError(_("Los parámetros deben ser números válidos."))

            # Filtrar por género si se proporciona
            domain = [('x_coordinate', '!=', False), ('y_coordinate', '!=', False)]
            if gender:
                domain.append(('gender', '=', gender))

            # Buscar contactos
            contacts = self.env['res.partner'].search(domain)

            # Calcular distancia para cada contacto
            close_contacts = []
            for contact in contacts:
                distance = self._calculate_distance(x_coordinate, y_coordinate, contact.x_coordinate, contact.y_coordinate)
                if distance <= max_distance:
                    close_contacts.append({
                        'name': contact.name,
                        'distance': distance,
                    })

            # Respuesta exitosa
            return {
                'success': True,
                'data': close_contacts,
            }

        except ValueError as e:
            # Error de tipo de dato
            return {
                'success': False,
                'error': str(e),
            }

        except Exception as e:
            # Error inesperado
            return {
                'success': False,
                'error': _("Ocurrió un error inesperado: %s") % e,
            }

    def _calculate_distance(self, x1, y1, x2, y2):
        # Fórmula de Haversine para calcular la distancia entre dos puntos
        from math import radians, sin, cos, acos

        # Convertir a radianes
        lat1 = radians(x1)
        lon1 = radians(y1)
        lat2 = radians(x2)
        lon2 = radians(y2)

        # Calcular diferencia de latitudes y longitudes
        dLat = lat2 - lat1
        dLon = lon2 - lon1

        # Calcular la distancia
        a = sin(dLat/2)**2 + cos(lat1) * cos(lat2) * sin(dLon/2)**2
        c = 2 * acos(sqrt(a))
        r = 6371 # Radio de la Tierra en kilómetros

        return c * r
