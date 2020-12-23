from django.urls import path
from .Scrape_View import Fetch


urlpatterns = [
  path('', Fetch.as_view(), name='search_view'),
  ]