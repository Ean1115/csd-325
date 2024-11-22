#Ean Masoner Module 7.2 Assignment test_cities.py
#Test_cities.py
import unittest
from City_Functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        formatted_string = city_country("Santiago", "Chile", 5000000, "Spanish")
        self.assertEqual(formatted_string, "Santiago, Chile - population 5000000, Spanish")
        formatted_string_with_population = city_country("Paris", "France", 2148327, "French")
        self.assertEqual(formatted_string_with_population, "Paris, France - population 2148327, French")

if __name__ == '__main__':
    unittest.main()