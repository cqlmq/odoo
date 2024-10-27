from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    custom_partner_field = fields.Char(string='自定义联系人字段')

    @api.model
    def custom_partner_method(self):
        # 自定义方法逻辑
        pass

