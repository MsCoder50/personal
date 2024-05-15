import geocoder
# import webbrowser
import folium

g = geocoder.ip('me')

myAddress = g.latlng
map = folium.Map(location=myAddress,scale_start= 4)
folium.CircleMarker(location=myAddress,radius=20, popup="Bhajanpura").add_to(map)
folium.Marker(location=myAddress).add_to(map)
map.save("map.html")