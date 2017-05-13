import time

from api_keys import F_CLIENT_ID, F_CLIENT_SECRET
from business import Business
import requests

SEARCH_URL = 'https://api.foursquare.com/v2/venues/explore?ll={},{}&intent=browse&radius={}&limit=50&query={}&client_id={}&client_secret={}&v={}'


def search(lat, lng, distance, query):
    """
    Searches the Foursquare API (Max Limit = 50)

    :param lat: Latitude of the request
    :param long: Longitude of the request
    :param distance: Distance to search (meters)
    :returns: List of retrieved venues
    """

    url = SEARCH_URL.format(lat, lng, distance,
                            query, F_CLIENT_ID, F_CLIENT_SECRET,
                            time.strftime("%Y%m%d"))
    venue_list = []
    try:
        data = requests.get(url).json()
        for i in range(0, 5):
            item = data['response']['groups'][0]['items'][i]
            venue = item['venue']
            venue_list.append(Business(venue['name'],
                                       venue['location']['address'],
                                       venue['rating'],
                                       venue['ratingSignals']))
    except Exception, e:
        print e

    return venue_list
