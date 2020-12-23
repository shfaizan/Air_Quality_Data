import requests
from bs4 import BeautifulSoup
from Global import AQUI_WEB_URL


# Air-Quality API helper service for querying API or WebScrapping Data
def get_gurugram_pollutants():
    # get the air quality index api url
    url = AQUI_WEB_URL
    try:
        response = requests.request("GET", url)
        status = response.status_code
        # api status
        if status == 200:
            # Parsing all the divs to get pollutant div and content
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
            # issue occurred and website didn't respond a 200
            """BAD REQUEST"""
            return False

    except Exception as stack_api_error:
        print(stack_api_error)
        return None