from django.conf.urls import url
from django.urls import path, include

from .views import (
        AirlineApiView,
        AirlineDetailApiView,
        AircraftApiView
)

urlpatterns = [
        path('', AirlineApiView.as_view()),
        path('<int:airline_idx>/' , AirlineDetailApiView.as_view()),
        path('aircraft/', AircraftApiView.as_view())
]



