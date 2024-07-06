import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

number="+919958496586"
key = "dadcecd7f2bc442e892bb5214fc2015e"

parsed_num= phonenumbers.parse(number)

location = geocoder.description_for_number(parsed_num, "en")
service_provider = carrier.name_for_number(parsed_num,"en")

# print(location)
# print(service_provider)

geocoder = OpenCageGeocode(key)

query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
# print([lat,lng])

map = folium.Map(location=[lat,lng],zoom_start=5)

folium.Marker(location=[lat,lng], popup=location).add_to(map)


map.save("map.html")
exit()