#Ean Masoner Module 7.2 CityFunction.py
# city_functions.py

def city_country(city, country, population, language):
    return f"{city}, {country} - population {population}, {language}"

# Calling the function three times
print(city_country("Santiago", "Chile", 5000000, "Spanish"))
print(city_country("Paris", "France", 2148327, "French"))
print(city_country("Tokyo", "Japan", 13929286, "Japanese"))