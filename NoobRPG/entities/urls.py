from django.urls import include, path
from entities import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'sellers', views.SellerViewSet)
router.register(r'npcs', views.NPCsViewSet)
router.register(r'players', views.PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework',
    )),
    path(
        'npcs/in_locations/<str:location_slug>/',
        views.NPCsInLocationViewSet.as_view({'get': 'list'}),
        name='npcs-in-location',
    ),
]
