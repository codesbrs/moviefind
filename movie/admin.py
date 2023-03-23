from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    pass
admin.site.register(Movie, MovieAdmin)

# Register your models here.
