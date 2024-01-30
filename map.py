import requests
from geopy.geocoders import GoogleV3
import folium
import os
from folium.plugins import MarkerCluster

def get_coordinates(api_key, location, city = ''):
    geolocator = GoogleV3(api_key=api_key)
    location_data = geolocator.geocode(location)
    
    if location_data:
        return location_data.latitude, location_data.longitude
    else:
        if city:
            location_data = geolocator.geocode(f'{city} {location}')
            if location_data:
                return location_data.latitude, location_data.longitude
        print(f"Couldn't find coordinates for {location}")
        return None

def create_map(api_key, attractions, city = '',enable_clustering=False):
    # Create a folium map centered around the first attraction
    first_attraction = attractions[0]
    map_center = get_coordinates(api_key, first_attraction, city)
    if map_center is None:
        return

    map_obj = folium.Map(location=map_center, zoom_start=12,)
    if enable_clustering:
        marker_cluster = MarkerCluster().add_to(map_obj)

    # Add markers for each attraction
    for i,attraction in enumerate(attractions):
        coords = get_coordinates(api_key, attraction)
        if coords:
            folium.Marker(coords, popup=attraction, icon=folium.Icon(color='red' if i>0 else 'blue')).add_to(marker_cluster if enable_clustering else map_obj)

    # Save the map to an HTML file
    fname = "clustered_tourist_map_1" if enable_clustering else "tourist_map_1"
    while(os.path.exists(f"{fname}.html")):
        fname = fname[:-1] + str(int(fname[-1]) + 1)
    map_obj.save(f"{fname}.html")
    print(f"Map created successfully. Open {fname} in your browser.")

if __name__ == "__main__":
    with open("api.txt") as f:
        api_key = f.read().strip()
    
    with open("attractions.txt",encoding='utf8') as f:
        attractions = f.read().strip().split("\n")

    if len(attractions) == 0:
        print("No attractions found. Exiting.")
        exit()

    if os.path.exists("city.txt"):
        with open("city.txt") as f:
            city = f.read().strip()

    create_map(api_key, attractions, city, enable_clustering=True)
