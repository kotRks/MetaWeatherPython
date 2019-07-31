import pytest
import unittest
from Req.app.WeatherFunction import WeatherFunction
import Req.values.testdata as test_data
import logging


testlog =  logging.getLogger('testlog')

class TestWeatherCases(unittest.TestCase):


    def setUp(self):
        self.client = WeatherFunction()

    def test_weather_by_city(self):
        test_item = self.client.getWeatherByCity(test_data.san_francisco['name'])
        self.assertIs(test_item.status_code, 200)
        self.assertIsNotNone(test_item.json())

    def test_weather_by_param(self):
        test_item = self.client.getWeatherByCity(test_data.san_francisco['name'])
        self.assertIs(test_item.status_code, 200)
        self.assertEqual(test_item.json()[0]["latt_long"], test_data.san_francisco['latt_long'])
        self.assertIsNotNone(test_item.json())

    def test_weather_by_woeid(self):
        test_item = self.client.getWeatherByWoeId(test_data.san_francisco['woeid'])
        self.assertIs(test_item.status_code, 200)
        self.assertIsNotNone(test_item.json()["consolidated_weather"][0]["weather_state_name"])
        self.assertIsNotNone(test_item.json()["consolidated_weather"][0]["wind_speed"])
        self.assertIsNotNone(test_item.json()["consolidated_weather"][0]["the_temp"])
        testlog.info('Log responce weather_state_name - ' + test_item.json()["consolidated_weather"][0]["weather_state_name"])
        testlog.info('Log responce wind_speed - ' + str(test_item.json()["consolidated_weather"][0]["wind_speed"]))
        testlog.info('Log responce the_temp - ' + str(test_item.json()["consolidated_weather"][0]["the_temp"]))

    def test_weather_by_woeid_on_date(self):
        search_time = test_data.bucharest_data["date"].split("-")
        search_time.reverse()
        searchig = '/'.join(search_time)
        date_for_filter = '-'.join(search_time) + 'T' + test_data.bucharest_data["time"]
        test_item = self.client.getWeatherByWoeIdOnDate(test_data.bucharest_data['woeid'], searchig)
        self.assertIs(test_item.status_code, 200)
        result_dates = test_item.json()
        created_dates = [row['created'] for row in result_dates]
        self.assertTrue(self.client.isDateInList(created_dates, date_for_filter))