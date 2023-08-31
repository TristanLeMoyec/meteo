
from meteo_v2 import convert_to_celsius

def test_convert_to_celsius():

    assert convert_to_celsius(0) == -273.15
    assert convert_to_celsius(273.15) == 0
    assert convert_to_celsius(373.15) == 100
