import unittest
from datetime import date, timedelta
from battery.spindler_battery import SpindlerBattery
     
class TestSplinderBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=3.5*365)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()