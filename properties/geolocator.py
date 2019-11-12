# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:57:34 2019
Add geolocation to database of items.csv based on street, city, and town.
@author: LindenMa01
"""
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time
import pandas as pd


# The geolocator uses OpenStreetMap Nominatim to find the geolocation.

def geolocator(street, city):
    geolocator = Nominatim(user_agent=user)
    # Comma seperation improves search result performance
    address = (street + ', ' + city)
    try:
        # First try based on address and city
        location = geolocator.geocode(address, timeout=10)
        # If address is not found, use only city
        if location is None:
            # OSM Usage Policy only allows for 1 request per second.
            time.sleep(1)
            location = geolocator.geocode(city, timeout=10)
            return location.latitude, location.longitude
            # If locationj is still non exitent return None for geolocation
            if location is None:
                return None, None
        else:
            return location.latitude, location.longitude
    except GeocoderTimedOut:
        print("OSM took too long to respond")

# OSM Usage Policy requires you to provide a valid HTTP Referer or User-Agent
with open('user_agent.txt') as agent:
    user = agent.read()

latitude = []
longitude = []

df = pd.read_csv('items.csv')

for row in df.index:
    street = df['street'][row]
    city = df['city'][row]
    lat, lon = geolocator(street, city)
    latitude.append(lat)
    longitude.append(lon)
    # OSM Usage Policy only allows for 1 request per second.
    time.sleep(1)

df['latitude'] = latitude
df['longitude'] = longitude

df.to_csv('items.csv')
