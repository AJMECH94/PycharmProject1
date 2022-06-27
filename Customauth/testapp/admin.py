from django.contrib import admin
from .models import MovieInfo,Mycollection

class MovieAdmin(admin.ModelAdmin):
    list_display = ['uid','Title']

class MycollectionAdmin(admin.ModelAdmin):
    list_display = ['Title']


admin.site.register(MovieInfo,MovieAdmin)
admin.site.register(Mycollection,MycollectionAdmin)
