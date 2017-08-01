# This file is part of the stock_move_warehouse module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockMoveWarehouseTestCase(ModuleTestCase):
    'Test Stock Move Warehouse module'
    module = 'stock_move_warehouse'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockMoveWarehouseTestCase))
    return suite
