import json
from pprint import pprint
import requests as re
from FlightData.models.flight_data_datamodel import CitiesDataModel


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.base_url = 'https://api.sheety.co/cb88ff219ca11ea79e72f9fec2a12a86/flightDeals/cities'

    def get_data(self) -> CitiesDataModel:
        response = re.get(self.base_url)
        data = response.json()
        return CitiesDataModel(**data)

    def put_data(self, id, data):
        url = f'{self.base_url}/{id}'
        body = json.dumps({"city": data})
        headers = {'Content-Type': 'application/json'}
        print(f'url: {url}')
        print(f'body: {body}')
        response = re.put(url=url, data=body,headers=headers)
        print(response.json())
        return response.json()
