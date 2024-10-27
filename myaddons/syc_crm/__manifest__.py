{
    'name': '思易创CRM扩展', 
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': '思易创CRM功能扩展，新增或修改了一些功能和视图 1.0',
    'description': """
        这个模块扩展了Odoo的CRM功能，特别是针对中国的CRM需求，新增或修改了一些功能和视图。
        同时也扩展了联系人功能。
    """,
    'author': '重庆思易创科技 提供',
    'website': 'https://www.siyic.cn',
    'license': 'OPL-1',  # 改为专有许可
    'price': 99.99,  # 设置模块价格
    'currency': 'EUR',  # 设置价格货币
    'live_test_url': 'https://www.siyic.cn/odoo/demo',  # 可选：添加演示链接
    'depends': ['crm', 'base'],
    'data': [
        'views/crm_lead_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'i18n': ['i18n/zh_CN.po'],
}
