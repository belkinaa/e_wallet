from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name', 'email')
    search_fields = ['name', 'email']

admin.site.register(User, UserAdmin)
