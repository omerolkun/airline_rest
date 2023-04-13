from django.conf.urls import url
from django.urls import path, include

from .views import (
        AirlineApiView,
)

urlpatterns = [
        path('', AirlineApiView.as_view()),
]



