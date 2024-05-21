# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint

from FlightData import DataManager
from FlightSearch import flight_search

''
if __name__ == '__main__':
    data_manager = DataManager.DataManager()
    fs = flight_search.CitySearch()
    cities = data_manager.get_data().cities
    for city in cities:
        if not city.iataCode:
            city_to_update = dict(city)
            new_iata_code = fs.get_destination_code(city.city)
            city_to_update['iataCode'] = fs.get_destination_code(city.city).locations[0].code
            data_manager.put_data(city.id, city_to_update)
