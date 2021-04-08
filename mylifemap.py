import folium
map = folium.Map(location=[42.065503036286756, -90.6765141173417], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[42.018879, -90.753932], popup="My Childhood Farm House", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[42.065300, -90.677113], popup="My Home During High School", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[42.002619, -90.605518], popup="My Elementary School: Delwood Elementary School", icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[42.063493, -90.664101], popup="My Middle School: Maquoketa Middle School", icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[42.059306, -90.672518], popup="My High School: Maquoketa High School", icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[41.993445, -90.737687], popup="My First Church: Elwood United Methodist Church", icon=folium.Icon(color='blue')))
fg.add_child(folium.Marker(location=[42.069168, -90.675114], popup="My Second Church: First Baptist", icon=folium.Icon(color='blue')))
fg.add_child(folium.Marker(location=[42.060972, -90.671211], popup="My Home Church: Faith Community Church", icon=folium.Icon(color='blue')))
fg.add_child(folium.Marker(location=[42.062625, -90.663144], popup="My Youth Group: The Lions Den", icon=folium.Icon(color='blue')))
fg.add_child(folium.Marker(location=[41.759665, -90.457964], popup="Best Catfishin' Hole in Iowa", icon=folium.Icon(color='pink')))
fg.add_child(folium.Marker(location=[42.021184, -90.809913], popup="Shot First Deer with Bow", icon=folium.Icon(color='pink')))
fg.add_child(folium.Marker(location=[41.694112, -90.585214], popup="Grandpa Dick's House", icon=folium.Icon(color='orange')))
fg.add_child(folium.Marker(location=[41.438638, -91.051200], popup="Grandma Harkey's House", icon=folium.Icon(color='orange')))




map.add_child(fg)

map.save("Map1.html")
