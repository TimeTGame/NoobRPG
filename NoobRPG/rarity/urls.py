from django.urls import include, path
from rarity import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', views.RarityViewSet, basename='rarity')

urlpatterns = [
    path('', include(router.urls)),
]
