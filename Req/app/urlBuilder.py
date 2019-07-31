class urlBuilder():

    def __init__(self):
        self.host: str = 'www.metaweather.com'

    def search_by_city(self, city: str) -> str:
        return f'https://{self.host}/api/location/search/?query={city}'

    def search_by_long_latt(self, long_latt) -> str:
        return f'https://{self.host}/api/location/search/?lattlong={long_latt}'

    def search_by_woeid(self, woeid: str) -> str:
        return f'https://{self.host}/api/location/{woeid}'

    def search_by_woeid_on_date(self, woeid:str, date:str) -> str:
        return f'https://{self.host}/api/location/{woeid}/{date}/'
