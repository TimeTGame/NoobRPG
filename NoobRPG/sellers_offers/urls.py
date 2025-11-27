from django.urls import include, path
from rest_framework import routers
from sellers_offers import views


router = routers.DefaultRouter()
router.register(r'', views.SellerOfferViewSet, basename='sellers-offers')

urlpatterns = [
    path('', include(router.urls)),
]
