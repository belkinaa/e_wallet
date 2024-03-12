from django import forms

class Get_walets_user(forms.Form):
    email = forms.CharField(label='Введите e-mail пользователя', max_length=255)