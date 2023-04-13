from django.contrib import admin
from django.urls import path, include
from airline import urls as airline_urls
from aircrafts import urls as aircraft_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('airline/', include(airline_urls)),
    path('aircraft/', include(aircraft_urls)),

]
