from django.contrib import admin

# Register your models here.
from .models import Wallet


class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency', 'owner', 'balance')
    list_display_links = ('id', 'currency', 'owner', 'balance')


admin.site.register(Wallet, WalletAdmin)