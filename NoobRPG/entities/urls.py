from django.urls import include, path
from entities import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'sellers', views.SellerViewSet, basename='sellers')
router.register(r'npcs', views.NPCsViewSet, basename='npcs')
router.register(r'players', views.PlayerViewSet, basename='players')

urlpatterns = [
    path('', include(router.urls)),
]
