import folium
import pandas

data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
map = folium.Map(location=[34.7, -94.06], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi! I'm a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map2.html")