import unittest
from engine.capulet_engine import CapuletEngine

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
        
if __name__ == '__main__':
    unittest.main()