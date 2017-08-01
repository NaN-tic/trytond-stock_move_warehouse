# This file is part stock_move_warehouse module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .move import *


def register():
    Pool.register(
        Move,
        module='stock_move_warehouse', type_='model')
