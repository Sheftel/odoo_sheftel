import random

from odoo import api, fields, models, SUPERUSER_ID, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Sales Order"
    _order = 'date_order desc, id desc'

    test = fields.Char(
        string="Test",
        default=random.random(),
        copy=False,
        compute="_test_quotation_update"
    )

    @api.depends("date_order", "amount_total")
    def _test_quotation_update(self):
        for record in self:
            record.test = f"{record.amount_total} - {record.date_order}"

    @api.onchange("test")
    def _test_text_too_big(self):
        for record in self:
            if len(record.test) > 50:
                return{
                    'warning': {
                        'title': 'Warning!',
                        'message': 'Длина текста должна быть меньше 50 символов'
                    }
                }


