# Copyright 2020 Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# imports propios de python
import json
from math import sqrt

# imports de odoo
from odoo import http
from odoo.http import request, Response
from odoo.exceptions import ValidationError

#imports de addons de odoo
from odoo.addons.base_rest.controllers import main

# La función distance recibe como parametros las coordenadas cartesianas x e y
# de dos puntos y retorna la distancia euclidiana entre estos puntos.
def distance(x1, y1, x2, y2):
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

class RestApiPublicController(main.RestController):
    _root_path = "/restapi/public/"
    _collection_name = "ccu.connector.rest.public.services"
    _default_auth = "public"
    _cors = "*"

class RestApiPrivateController(main.RestController):
    _root_path = "/restapi/private/"
    _collection_name = "ccu.connector.rest.private.services"
    _default_auth = "api_key"
    _cors = "*"

# Se crea la classe ContactController que se encargará de manejar las peticiones
# recibidas.
class ContactController(http.Controller):
    @http.route('/contact/close_contact', type='http', auth='public', methods=['GET'])
    def close_contact(self, **kwargs):
        try:
            # Se obtiene el valor de los parámetros de la solicitud.
            x_coordinate = float(kwargs.get('x_coordinate'))
            y_coordinate = float(kwargs.get('y_coordinate'))
            max_distance = float(kwargs.get('max_distance'))
            gender = kwargs.get('gender')

            # Se verifica que los parámetros obligatorios vengan en la solicitud.
            # En caso de que falte un parametro se responde un JSON y status 400.
            if not all([x_coordinate, y_coordinate, max_distance]):
                raise ValidationError('Missing required parameters')
            
            # Si no faltan parametros requeridos se procede a  filtrar los contactos
            # por coordenadas primeramente y luego, si viene definido el parametro gender
            # en la solicitud se añade a los filtros a aplicar.
            domain = [
                ('x_coordinate', '<=', x_coordinate + max_distance),
                ('x_coordinate', '>=', x_coordinate - max_distance),
                ('y_coordinate', '<=', y_coordinate + max_distance),
                ('y_coordinate', '>=', y_coordinate - max_distance),
            ]
            if gender:
                domain.append(('gender', '=', gender))
            
            #Se hace la consulta mediante le ORM y los filtros establecidos previamente.
            contacts = request.env['res.partner'].sudo().search(domain)

            # A los contactos que pasan los filtros, se les calcula la distancia con respecto
            # a las coordenadas dadas en la solicitud  mediante la funcion *distance* ya definida.
            # Los contactos que cumplen, se agregan a una lista en forma de objeto con los campos 
            # name y distance.
            close_contacts = []
            for contact in contacts:
                distance_to_contact = distance(x_coordinate, y_coordinate, contact.x_coordinate, contact.y_coordinate)
                if distance_to_contact <= max_distance:
                    close_contacts.append({
                        'name': contact.name,
                        'distance': distance_to_contact
                    })
            
            # Posteriormente, se arma un objeto con los campos success, error y data,
            # donde en data se agregar los contactos resultantes
            response_data = {
                'success': True,
                'error': None,
                'data': close_contacts
            }
            
            # Finalmente se envía un JSON con el objeto mencionado y un codigo de stado 200.
            return Response(json.dumps(response_data), content_type='application/json', status=200)
        
        #A continuación se puede ver el manejo de excepciones.
        except ValueError as ve:
            response_data = {
                'success': False,
                'error': 'Invalid parameter value: ' + str(ve),
                'data': []
            }
            return Response(json.dumps(response_data), content_type='application/json', status=400)
        
        except ValidationError as ve:
            response_data = {
                'success': False,
                'error': str(ve),
                'data': []
            }
            return Response(json.dumps(response_data), content_type='application/json', status=400)
        
        except Exception as e:
            response_data = {
                'success': False,
                'error': 'An error occurred: ' + str(e),
                'data': []
            }
            return Response(json.dumps(response_data), content_type='application/json', status=500)