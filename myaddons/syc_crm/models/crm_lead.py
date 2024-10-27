from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    custom_field = fields.Char(string='自定义字段')

    @api.model
    def custom_method(self):
        # 自定义方法逻辑
        pass
