from odoo import exceptions, http, models
from odoo.http import request
class IrHttp(models.AbstractModel):
    _name = 'ir.http'
    _inherit = 'ir.http'
    def _auth_method_my_pet_group_admin(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>",self)
        self._auth_method_user()
        if not request.env.user.has_group('my_pet_group_admin'):
            raise exceptions.AccessDenied()