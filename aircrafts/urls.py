from django.conf.urls import url
from django.urls import path, include

from .views import (
        AircraftApiView,
        AircraftDetailApiView
)

urlpatterns = [
        path('', AircraftApiView.as_view()),
        path('<int:aircraft_idx>/' , AircraftDetailApiView.as_view()),

]



