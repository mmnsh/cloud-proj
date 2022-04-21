from django.urls import path
from apis1.views import GetAllData, first, second, third, forth, fifth

urlpatterns = [
    path('get-all-data/', GetAllData.as_view()),
    #path('get-some-data-1/', GetAllFlightsFromSpecialAirportData.as_view()),
    path('get-first/', first.as_view()),
    path('get-second/', second.as_view()),
    path('get-third/', third.as_view()),
    path('get-forth/', forth.as_view()),
    path('get-fifth/', fifth.as_view()),
    ]