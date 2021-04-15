import folium
import pandas

data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation <= 2000:
        return 'orange'
    elif elevation <= 3000:
        return 'blue'
    else:
        return 'red'

map = folium.Map(location=[34.7, -94.06], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 14, popup=str(el)+" m", fill_color=color_producer(el), color = 'white', fill_opacity = 0.6))


fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'yellow'}))

map.add_child(fg)
map.save("Map3.html")