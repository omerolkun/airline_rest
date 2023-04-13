from django.conf.urls import url
from django.urls import path, include

from .views import (
        AircraftApiView
)

urlpatterns = [
        path('', AircraftApiView.as_view()),
]



