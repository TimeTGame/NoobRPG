from django.urls import include, path
from items import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', views.ItemViewSet, basename='items')

urlpatterns = [
    path('items/', include(router.urls)),
]
