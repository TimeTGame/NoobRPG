from django.urls import include, path
from locations import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', views.LocationViewSet, basename='location')

urlpatterns = [
    path('', include(router.urls)),
]
