from django.urls import path
from .views import get_water_data, get_water_quality, get_cities_data, previousmonth_leakage, monthlylimit_consumption, yearlylimit_consumption

urlpatterns = [
    path('water-data/', get_water_data, name='water-data'),
    path('water-purify/', get_water_quality, name='water-quality'),
    path('citydata/', get_cities_data, name='city-data'),
    path('prevmonth/', previousmonth_leakage, name='previous-month-leakage'),
    path('monthlylc/', monthlylimit_consumption, name='monthly-limit-consumption'),
    path('yearlylc/', yearlylimit_consumption, name='yearly-limit-consumption'),
]
