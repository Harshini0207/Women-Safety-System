import pandas as pd
import folium

def generate_map():

    data = pd.read_csv("crime_data.csv")

    m = folium.Map(location=[17.3850, 78.4867], zoom_start=12)

    for i in range(len(data)):

        risk = data.iloc[i]["Risk_Level"]

        if risk == "high":
            color = "red"
        elif risk == "medium":
            color = "orange"
        else:
            color = "green"

        folium.Marker(
            location=[data.iloc[i]["latitude"], data.iloc[i]["longitude"]],
            popup=data.iloc[i]["location"] + " - " + risk,
            icon=folium.Icon(color=color, icon="exclamation-sign")
        ).add_to(m)

    m.save("templates/map.html")

generate_map()