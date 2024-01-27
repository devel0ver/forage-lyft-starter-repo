import unittest
from tires.octoprime_tires import OctoprimeTires

class TestOctoprime(unittest.TestCase):
    def test_octoprime_needs_service(self):
        wear_level = [0.9, 0.6, 0.8, 0.8]
        tire = OctoprimeTires(wear_level)
        self.assertTrue(tire.needs_service())
        
    def test_octoprime_does_not_need_service(self):
        wear_level = [0.5, 0.7, 0.3, 0.9]
        tire = OctoprimeTires(wear_level)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()