from django import forms
from online_wallet.models import Wallet
class Get_walets_user_form(forms.Form):
    email = forms.CharField(label='Введите e-mail пользователя', max_length=255)

class Get_walet_form(forms.Form):
    id_wallet = forms.ChoiceField(label='выберите кошелек пользователя', choices=[(item.id, f'{item.owner} {item.currency}') for item in Wallet.objects.all()])

