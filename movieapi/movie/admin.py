from django.contrib import admin
from .models import MovieList,Watch,PopularList

admin.site.register(MovieList)
admin.site.register(Watch)
admin.site.register(PopularList)