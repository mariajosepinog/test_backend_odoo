# Copyright 2020 Open Source intgerators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo.addons.component.core import Component
from odoo.addons.base_rest import restapi
import logging
import re

_logger = logging.getLogger(__name__)
class Account(Component):

    _inherit = "base.rest.service"
    _name = "contact.service"
    _usage = "contact"
    _collection = "ccu.connector.rest.public.services"
    _cors = "*"
    _description =  """
                    Contact Queries
                    ===============
                    Endpoints available:
                    * ``GET /restapi/public/contact/close_contact``: get close contacts sorted
                    """
    # Definicion de método GET y respectivos parametros
    @restapi.method(
        [(["/<int:x_coordinate>/<int:y_coordinate>"], "GET")],
        auth="public",
    )
    # Creación de función para retornar usuarios que cumplan con max_distance
    def searchByCoordinate(self, x_coordinate,y_coordinate):
        try:
            partner_list = []
            
            partner_dict = {}
            
            max_distance = x_coordinate + y_coordinate
            
            partners = self.env["res.partner"].search([])
            
            for i in partners:
                if i.x_coordinate + i.y_coordinate == max_distance:
                    partner_dict = {
                        "name": i.name
                    }
                    partner_list.append(partner_dict)
            return{
            "Success":True,
            "error":"No existe error",
            "data": partner_list
            }
        except Exception as e:
            return{
            "Success":False,
            "error":e,
            "data": []
            }