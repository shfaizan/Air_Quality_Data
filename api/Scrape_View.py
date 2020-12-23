from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Scrape.WebScraping import  get_gurugram_pollutants


class Fetch(APIView):
    def get(self, request):
        data = get_gurugram_pollutants()
        return Response(data=data, status=status.HTTP_200_OK)
