from django.urls import path
from game import views


urlpatterns = [
    path(
        'change-location/',
        views.ChangeLocationView.as_view(),
        name='change-location',
    ),
    path(
        'start-battle/',
        views.StartBattleView.as_view(),
        name='start-battle',
    ),
    path(
        'attack/',
        views.AttackView.as_view(),
        name='attack',
    ),
]
