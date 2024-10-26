from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # 添加新字段
    custom_field = fields.Char(string='自定义字段')

    # 添加新的方法
    @api.model
    def custom_method(self):
        # 自定义逻辑
        pass
