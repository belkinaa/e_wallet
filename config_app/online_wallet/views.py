from django.shortcuts import render
from django.http import HttpResponse
from .forms import Get_walets_user_form, Get_walet_form
from .models import Wallet, User
# Create your views here.

def card_wallet(request):
    page_info = {
        'form': Get_walet_form()
    }
    if (request.method == 'POST'):
        form = Get_walet_form(request.POST)
        page_info.update({'form': form})
        print('form:', form)
        if form.is_valid():
            page_info.update({'id_wallet': (id_wallet := form.cleaned_data.get('id_wallet'))})

            page_info.update({'walet': Wallet.objects.filter(id=id_wallet).first()})

    return render(request, "wallet/card_wallet.html", page_info)

def card_users(request):
    page_info = {
        'form': Get_walets_user_form()
    }
    if (request.method == 'POST'):
        form = Get_walets_user_form(request.POST)
        page_info.update({'form': form})
        if form.is_valid():
            page_info.update({'email': (email := form.cleaned_data.get('email'))})
            if (is_user:= User.object.filter(email=email).first()):
                if (is_wallets := Wallet.objects.filter(owner=is_user).all()):
                    page_info.update({'walets': is_wallets})
    return render(request, "wallet/card_user.html", page_info)