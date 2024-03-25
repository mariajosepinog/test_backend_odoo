# Copyright (C) 2019 Open Source Integrators
# <https://www.opensourceintegrators.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Test Contacts',
    'version': '12.0.0.0.0',
    'license': 'AGPL-3',
    'summary': 'Test Contacts',
    'author': 'Desarrollo CCU S.A.',
    'website': '',
    'depends': [
        "base",
        "base_rest",
        "component",
        "contacts",
    ],
    # Se agregan tanto los cambios a la vista como los archivos de ejemplo
    'data': [
        'data/res_partner.xml',
        'views/res_partner.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
