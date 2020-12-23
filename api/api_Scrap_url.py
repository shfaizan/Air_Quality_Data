from django.urls import path
from .api_Scrape_view import Fetch


urlpatterns = [
  path('', Fetch.as_view(), name='search_view'),
  ]