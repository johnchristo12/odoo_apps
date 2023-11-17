# -*- coding: utf-8 -*-
from odoo import models, api, fields, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for transfer in self.picking_ids:
            for line in transfer.move_ids_without_package:
                line.quantity_done = line.product_uom_qty
            transfer.action_assign()
            transfer.button_validate()
        self._create_invoices()
        return res
