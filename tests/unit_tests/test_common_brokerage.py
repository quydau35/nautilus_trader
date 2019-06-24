#!/usr/bin/env python3
# -------------------------------------------------------------------------------------------------
# <copyright file="test_brokerage.py" company="Nautech Systems Pty Ltd">
#  Copyright (C) 2015-2019 Nautech Systems Pty Ltd. All rights reserved.
#  The use of this source code is governed by the license as found in the LICENSE.md file.
#  http://www.nautechsystems.io
# </copyright>
# -------------------------------------------------------------------------------------------------

import unittest

from nautilus_trader.model.objects import Quantity, Money, Price
from nautilus_trader.common.brokerage import CommissionCalculator
from test_kit.stubs import TestStubs

GBPUSD_FXCM = TestStubs.instrument_gbpusd().symbol
USDJPY_FXCM = TestStubs.instrument_usdjpy().symbol


class CommissionCalculatorTests(unittest.TestCase):

    def test_can_calculate_correct_commission(self):
        # Arrange
        calculator = CommissionCalculator()

        # Act
        result = calculator.calculate(
            GBPUSD_FXCM,
            Quantity(1000000),
            filled_price=Price('1.63000'),
            exchange_rate=1.00)

        # Assert
        self.assertEqual(Money(32.60), result)

    def test_can_calculate_correct_minimum_commission(self):
        # Arrange
        calculator = CommissionCalculator()

        # Act
        result = calculator.calculate_for_notional(
            GBPUSD_FXCM,
            Money(1000))

        # Assert
        self.assertEqual(Money(2.00), result)

    def test_can_calculate_correct_commission_for_notional(self):
        # Arrange
        calculator = CommissionCalculator()

        # Act
        result = calculator.calculate_for_notional(
            GBPUSD_FXCM,
            Money(1000000))

        # Assert
        self.assertEqual(Money(20.00), result)

    def test_can_calculate_correct_commission_with_exchange_rate(self):
        # Arrange
        calculator = CommissionCalculator()

        # Act
        result = calculator.calculate(
            USDJPY_FXCM,
            Quantity(1000000),
            filled_price=Price('95.000'),
            exchange_rate=0.01052632)

        # Assert
        self.assertEqual(Money(20.00), result)
