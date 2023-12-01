import unittest
from datetime import datetime, timedelta
from .Battery import NubbinBattery, SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        # Test the case where the battery needs service
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2018, 1, 1)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(nubbin_battery.needs_service())

        # Test the case where the battery does not need service
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbin_battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        # Test the case where the battery needs service
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2020, 1, 1)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service())

        # Test the case where the battery does not need service
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service())

if __name__ == '__main__':
    unittest.main()
