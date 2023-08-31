import streamlit as st
import requests
import os
from dotenv import load_dotenv
import folium
from streamlit_folium import folium_static

# charger les variables d'environement à partir du fichier .env
load_dotenv()

# Accéder aux valeurs des variables d'environnement
api_key = os.environ['API_KEY']

# Access environment variables
API_KEY = os.getenv("API_KEY")

# Fonction pour convertir la température de Kelvin en Celsius
def convert_to_celsius(temperature_in_kelvin):
    return temperature_in_kelvin - 273.15

# Fonction pour obtenir les informations météorologiques actuelles d'une ville
def find_current_weather(city):
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    weather_data = requests.get(base_url).json()
    try:
    # Récupération des informations météorologiques à partir de la réponse JSON
        general = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(convert_to_celsius(weather_data['main']['temp']))
        max_temperature = round(convert_to_celsius(weather_data['main']['temp_max']))
        feels_temp = round(convert_to_celsius(weather_data['main']['feels_like']))
        humidity = weather_data['main']['humidity']
        icon = f'https://openweathermap.org/img/wn/{icon_id}@2x.png'
        coords = weather_data['coord']
    except KeyError:
    # Afficher un message d'erreur si la ville n'est pas trouvée
        st.error('City Not Found')
        st.stop()
    return general, temperature, max_temperature, feels_temp, humidity, icon, coords

# Fonction principale
def main():
    st.header(':cherry_blossom: Météo Club :cherry_blossom:')
    city = st.text_input("Enter the city").lower()

    if st.button('Find'):
        # Appel à la fonction pour obtenir les informations météorologiques
        general, temperature, max_temperature, feels_temp, humidity, icon, coords = find_current_weather(city)
        # Afficher une carte avec la localisation de la ville
        map_center = [coords['lat'], coords['lon']]
        m = folium.Map(location=map_center, zoom_start=10)
        folium.Marker(map_center, popup=city.capitalize()).add_to(m)
        folium_static(m)  # Afficher la carte dans Streamlit

        # Diviser la mise en page en trois colonnes
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('Temperature', str(temperature)+'℃', str(max_temperature-temperature)+'℃')
            st.metric('Feels Like', str(feels_temp)+'℃')
        with col2:
            st.metric('Humidity', str(humidity)+'%')
        with col3:
            st.write(general)
            st.image(icon)

if __name__ == '__main__':
    main()
