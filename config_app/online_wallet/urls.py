from django.urls import path
from .views import wallet, card_users

urlpatterns = [
    path('', wallet),
    path('wallet/', wallet),
    path('card_users/', card_users),
]