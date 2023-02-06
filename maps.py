import googlemaps
import os
import pprint
from colorama import Fore


def location_from_address(address):
    # configure the google maps api
    api_key = os.getenv("GOOGLE_API_KEY")
    gmaps = googlemaps.Client(key=f"{api_key}")
    # Geocode an address
    geocode_result = gmaps.geocode(address)
    located_address = geocode_result[0]["geometry"]["location"]

    # Print the result
    pprint.pprint(
        Fore.BLUE + f"Located address: {located_address}" + Fore.RESET)
    return located_address
