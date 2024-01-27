import unittest
from tires.carrigan_tires import CarriganTires

class TestCarrigan(unittest.TestCase):
    def test_octoprime_needs_service(self):
        wear_level = [0.9, 0.7, 0.7, 0.8]
        tire = CarriganTires(wear_level)
        self.assertTrue(tire.needs_service())
        
    def test_octoprime_does_not_need_service(self):
        wear_level = [0.5, 0.7, 0.3, 0.8]
        tire = CarriganTires(wear_level)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()