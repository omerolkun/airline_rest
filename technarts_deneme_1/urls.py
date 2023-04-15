from django.contrib import admin
from django.urls import path, include
from airline import urls as airline_urls
from aircrafts import urls as aircraft_urls
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('airline/', include(airline_urls)),
    path('aircraft/', include(aircraft_urls)),
    path('api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
