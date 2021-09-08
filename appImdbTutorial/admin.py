from django.contrib import admin
from .models import Actor, Film, AdditionalInfo, Rating

# Register your models here.
#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin) :
    # fields = ['title', 'year', 'description']
    # exclude = ['description']
    list_display = ['title', 'imdb_rating', 'year']
    list_filter = ('year','release')
    search_fields = ('title', 'year')

admin.site.register(AdditionalInfo)
admin.site.register(Rating)
admin.site.register(Actor)