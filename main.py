import folium
map = folium.Map(location=[42.065503036286756, -90.6765141173417], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[41.8, -90.2], popup="Hi! I'm a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
