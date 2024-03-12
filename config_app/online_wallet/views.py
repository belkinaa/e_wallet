from django.shortcuts import render
from django.http import HttpResponse
from .forms import Get_walets_user
from .models import Wallet, User
# Create your views here.

def wallet(request):
    return HttpResponse("<h1>Hi!</h1>")

def card_users(request):
    user_info = {
        'form': Get_walets_user()
    }
    if (request.method == 'POST'):
        form = Get_walets_user(request.POST)
        user_info.update({'form': form})
        if form.is_valid():
            user_info.update({'email': (email := form.cleaned_data.get('email'))})
            if (is_user:= User.object.filter(email=email).first()):
                if (is_wallets := Wallet.objects.filter(owner=is_user).all()):
                    user_info.update({'walets': is_wallets})
    return render(request, "wallet/card_user.html", user_info)