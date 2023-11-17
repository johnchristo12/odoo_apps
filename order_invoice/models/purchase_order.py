# -*- coding: utf-8 -*-
from odoo import models, api, fields, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        for transfer in self.picking_ids:
            for line in transfer.move_ids_without_package:
                line.quantity_done = line.product_uom_qty
            transfer.action_assign()
            transfer.button_validate()
        self.action_create_invoice()
        return res
