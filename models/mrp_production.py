# Copyright 2016 Antiun Ingenieria S.L. - Javier Iniesta
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class MrpProduction(models.Model):
    _inherit = "mrp.production"
    _name = "mrp.production"
    _description = ""

    order_classification = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')],
        string="Order",
        default="A")

    def _get_move_raw_values(self, product_id, product_uom_qty, product_uom, operation_id=False, bom_line=False):
        res = super()._get_move_raw_values(product_id, product_uom_qty, product_uom, operation_id, bom_line)
        res['location_dest_id'] = self.location_src_id.id
        return res

    def _get_move_finished_values(self, product_id, product_uom_qty, product_uom, operation_id=False, byproduct_id=False):
        res = super()._get_move_finished_values(
            product_id, product_uom_qty, product_uom, operation_id, byproduct_id)
        res['location_id'] = self.location_src_id.id
        return res
