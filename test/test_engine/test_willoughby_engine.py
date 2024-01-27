import unittest
from engine.willoughby_engine import WilloughbyEngine


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
    
if __name__ == '__main__':
    unittest.main()