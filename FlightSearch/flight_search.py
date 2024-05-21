from datetime import datetime, timedelta
from pprint import pprint

import requests as re
from FlightSearch.models.CitySearchModel import CitySearchModel
from FlightSearch.models.FlightSearchModel import FlightDetail


class CitySearch:
    def __init__(self):
        self.base_url = 'https://api.tequila.kiwi.com/'
        self.api_key = ''

    def get_destination_code(self, data: str) -> CitySearchModel:
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
        return CitySearchModel(**results)


class FlightSearch:
    def __init__(self):
        self.base_url = 'https://api.tequila.kiwi.com'
        self.api_key = ''

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time) -> FlightDetail:
        headers = {"apikey": self.api_key}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 20,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = re.get(
            url=f"{self.base_url}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()['data'][0]
            print(len(response.json()['data']))
            return response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        # print(f"{flight_data.destination_city}: £{flight_data.price}")
        # return flight_data


fs = FlightSearch()
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
values = fs.check_flights(origin_city_code='BUE', destination_city_code='BRC', from_time=tomorrow, to_time=six_month_from_today)

pprint(values)
