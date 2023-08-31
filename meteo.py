import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static


def main() :

    #à remplacer par récupération du json via api
    city_data = {
            "City": ["Paris", "Lyon", "Marseille"],
            "Latitude": [48.8566, 45.75, 43.2965],
            "Longitude": [2.3522, 4.85, 5.3698],
            "Temperature" : [20,25,35]
        }

    #Dataframe avec choix des colonnes qui nous intéressent
    df = pd.DataFrame(city_data)

    #titre
    st.title(':cherry_blossom: Météo Club :cherry_blossom:')

    #Choix de la ville
    city = st.selectbox(
        'Choisir la ville :',
        df['City'])

    #Filtre du df sur la ville selectionnée
    selected_city = df[df["City"] == city]

    #Coordonnées et température de la ville
    temperature = selected_city["Temperature"].values[0]
    latitude = selected_city["Latitude"].values[0]
    longitude = selected_city["Longitude"].values[0]


    #Map
    m = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup=city).add_to(m)

    folium_static(m)

    #Température avec barre de progrès (pas trouvé quelque chose qui ressemble à un thermomètre)
    st.write(f"Température à {city}: {temperature}°C")
    st.write("Thermomètre")
    st.progress(temperature / 50)

    #bouton soumettre, pour l'instant inutile
    if st.button("Soumettre"):
        st.text("Soumission")

if __name__ == "__main__":
    main()
