import unittest
from datetime import date, timedelta
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestCapuletEngine(unittest.TestCase):
    # capulet engine needs change every 30000
    def test_engine_needs_service(self):
        current_mileage = 33000
        last_service_mileage = 2000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        print(f'Test Capulet Engine: Last Service Mileage: {last_service_mileage}, Needs Service: {engine.needs_service()}')
        self.assertTrue(engine.needs_service())
    
    def test_engine_does_not_need_service(self):
        current_mileage = 22000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        print(f'Test Capulet Engine: Last Service Mileage: {last_service_mileage}, Needs Service: {engine.needs_service()}')
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mileage = 70000
        last_service_mileage = 5000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        print(f'Test Willoughby Engine: Last Service Mileage: {last_service_mileage}, Needs Service: {engine.needs_service()}')
        self.assertTrue(engine.needs_service())
        
    def test_engine_does_not_need_service(self):
        current_mileage = 65000
        last_service_mileage = 30000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        print(f'Test Willoughby Engine: Last Service Mileage: {last_service_mileage}, Needs Service: {engine.needs_service()}')
        self.assertFalse(engine.needs_service())
    
class TestSternmanEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        print(f'Test Sternman Engine: Warning light on: {warning_light_is_on}, Needs Service: {engine.needs_service()}')
        self.assertTrue(engine.needs_service())
        
    def test_engine_does_not_need_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        print(f'Test Sternman Engine: Warning light on: {warning_light_is_on}, Needs Service: {engine.needs_service()}')
        self.assertFalse(engine.needs_service())
        
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

class TestSplinderBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=3*365)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()