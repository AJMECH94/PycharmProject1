from django.contrib import admin
from .models import UserInfo
# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(UserInfo,UserInfoAdmin)