import unittest
from engine.sternman_engine import SternmanEngine

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
      
if __name__ == '__main__':
    unittest.main()