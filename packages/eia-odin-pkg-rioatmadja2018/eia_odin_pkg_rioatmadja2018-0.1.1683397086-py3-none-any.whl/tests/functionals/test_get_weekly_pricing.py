#!/usr/bin/env python3
from unittest import TestCase
from eia.db.odin_pricing import OdinPricing
from eia.utils.credentials import load_credentials
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class TestWeeklyPricing(TestCase):

    def test_get_weekly_pricing(self):
        load_credentials()
        odin: 'OdinPricing' = OdinPricing()
        n_rows: 'DataFrame' = odin.get_weekly_pricing(state='washington').shape[0]
        log.debug("[ 15 ] %s" % (n_rows) )
        self.assertEqual(n_rows, 1616)