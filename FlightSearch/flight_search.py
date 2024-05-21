from pprint import pprint

import requests as re
from FlightSearch.models.filghtSearchModel import FlightSearchModel


class FlightSearch:
    def __init__(self):
        self.base_url = 'https://api.tequila.kiwi.com/'
        self.api_key = 'WTY_m0ICVqfVqwHr6uDrKdbHgOG5KPD7'

    def get_data(self, data: str) -> FlightSearchModel:
        # include api_key on the headers
        headers = {'apikey': self.api_key}
        url = self.base_url + 'locations/query/'
        query = {'term': data,
                 'locale': 'en-US',
                 'location_types': 'city',
                 'limit': 10,
                 'active_only': True}
        response = re.get(url, headers=headers, params=query)
        results = response.json()
        return FlightSearchModel(**results)


