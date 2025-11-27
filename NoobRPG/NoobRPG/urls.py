from django.contrib import admin
from django.urls import include, path, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/entities/', include('entities.urls')),
    path('api/v1/items/', include('items.urls')),
    path('api/v1/locations/', include('locations.urls')),
    path('api/v1/rarity/', include('rarity.urls')),
    path('api/v1/sellers_offers/', include('sellers_offers.urls')),
]
