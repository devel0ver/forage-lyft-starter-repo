import unittest
from datetime import date, timedelta
from battery.nubbin_battery import NubbinBattery
     
class TestNubbinBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=5*365)
        battery = NubbinBattery(last_service_date, current_date)
        print(f"Test Nubbin Battery: Last Service Date: {last_service_date}, Needs Service: {battery.needs_service()}")
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=2*365)
        battery = NubbinBattery(last_service_date, current_date)
        print(f"Test Nubbin Battery: Last Service Date: {last_service_date}, Needs Service: {battery.needs_service()}")
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()