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
    

