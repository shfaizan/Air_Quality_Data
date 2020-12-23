from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Scrape.WebScraping import  get_gurugram_pollutants
import datetime
'''
This is GET and POST request api for the display 

Endpoint for fetching pollutant data of gurugram (GET) - http://127.0.0.1:8000/fetch/'
Endpoint for fetching AQI data for all states of india (POST) - http://127.0.0.1:8000/fetch/

'''


class Fetch(APIView):
    def get(self, request):
        data = get_gurugram_pollutants()
        return Response(data=data, status=status.HTTP_200_OK)
