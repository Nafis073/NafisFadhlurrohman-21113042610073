def city_country(city, country):
    """Mengembalikan nama kota dan negara."""
    return f"{city.title()}, {country.title()}"

from city_functions import city_country

def test_city_country():
    hasil = city_country("santiago", "chile")

    assert hasil == "Santiago, Chile"