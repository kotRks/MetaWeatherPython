import requests
import urllib3

from Req.app.urlBuilder import urlBuilder

class WeatherFunction(object):

    def __init__(self):
        self.urls = urlBuilder()

    def _makeGetRequest(self, url: str):
        result = requests.get(url)
        return result

    def getWeatherByCity(self, search_city: str):
        request_url = self.urls.search_by_city(search_city)
        return self._makeGetRequest(request_url)

    def getWeatherByAttributes(self, attributes):
        request_url = self.urls.search_by_long_latt(attributes)
        return self._makeGetRequest(request_url)

    def getWeatherByWoeId(self, woeid: str):
        request_url = self.urls.search_by_woeid(woeid)
        return self._makeGetRequest(request_url)

    def getWeatherByWoeIdOnDate(self, woeid:str, date: str):
        request_url = self.urls.search_by_woeid_on_date(woeid, date)
#        return request_url
        return self._makeGetRequest(request_url)

    def isDateInList(self, dates_list: dict, search_date_time: str):
        for row in dates_list:
            if row.find(search_date_time) != -1:
                return True
        return False