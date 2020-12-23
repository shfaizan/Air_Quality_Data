from django.shortcuts import render
import requests
from Sevices.WebScraping import get_gurugram_pollutants


def index(request):
    pollutants = get_gurugram_pollutants()
    return render(request, 'template.html', {'dict': pollutants})