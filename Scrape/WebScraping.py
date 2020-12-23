import requests
from bs4 import BeautifulSoup


def get_gurugram_pollutants():
    url = "https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us"

    response = requests.request("GET", url)
    status = response.status_code
    if status == 200:
        pollutants = dict()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.findAll("div", {"class": "pollutant-item odd"})
        for result in results:
            name = result.find('div', attrs={'class': 'name'}).text
            value = result.find('div', attrs={'class': 'value'}).text
            pollutants[name] = value
        results = soup.findAll("div", {"class": "pollutant-item even"})
        for result in results:
            name = result.find('div', attrs={'class': 'name'}).text
            value = result.find('div', attrs={'class': 'value'}).text
            pollutants[name] = value
        return pollutants
    else:
        return False

