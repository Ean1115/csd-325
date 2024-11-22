#Ean Masoner Module 7.2 Assignment test_cities.py
#Test_cities.py
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        formatted_string = city_country("Santiago", "Chile")
        self.assertEqual(formatted_string, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()
