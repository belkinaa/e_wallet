from django.urls import path
from .views import card_wallet, card_users

urlpatterns = [
    path('', card_wallet),
    path('card_wallet/', card_wallet),
    path('card_users/', card_users),
]