# This file is part stock_move_warehouse module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Move']
__metaclass__ = PoolMeta


class Move:
    __name__ = 'stock.move'
    warehouse = fields.Function(fields.Many2One('stock.location',
            'Warehouse'), 'get_warehouse')

    def get_warehouse(self, name):
        if self.shipment and hasattr(self.shipment, 'warehouse'):
            return self.shipment.warehouse.id if self.shipment.warehouse else None
        return None
