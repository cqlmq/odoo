{
    'name': '思易创CRM扩展',  # 更新为中文名称
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': '思易创CRM功能扩展，新增或修改了一些功能和视图',
    'description': """
        这个模块扩展了Odoo的CRM功能，特别是针对中国的CRM需求，新增或修改了一些功能和视图。
    """,
    'depends': ['crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
