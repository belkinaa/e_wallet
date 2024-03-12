from django.urls import path
from .views import wallet, users

urlpatterns = [
    path('', wallet),
    path('wallet/', wallet),
    path('users/', users),
]