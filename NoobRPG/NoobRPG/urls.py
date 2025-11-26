from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('entities/', include('entities.urls')),
    path('locations/', include('locations.urls')),
]
