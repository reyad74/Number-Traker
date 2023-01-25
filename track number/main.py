import phonenumbers
import opencage
import folium
from phone import number
from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)
from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))
from opencage.geocoder import OpenCageGeocode
key = '39e52ce88ab8467682b32f036b69ec16'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)
myMap = folium.Map(location=[lat,lng],zoom_start=8)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("mylocation.html")