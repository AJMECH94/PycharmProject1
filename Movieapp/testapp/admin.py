from django.contrib import admin
from .models import MovieInfo,Mycollection,Profile
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['uid','Title']

class MycollectionAdmin(admin.ModelAdmin):
    list_display = ['Title']

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['name','email','username','Phone']

admin.site.register(Profile)
admin.site.register(MovieInfo,MovieAdmin)
admin.site.register(Mycollection,MycollectionAdmin)
