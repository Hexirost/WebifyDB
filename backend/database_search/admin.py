from django.contrib import admin
# from .models import characters

# class DatabseSearchAdmin(admin.ModelAdmin):
#     list_display = ( 'Name', 'ChapterReveal', 'EpisodeReveal', 'YearReveal', 'Notes' )

# # Register your models here.

# admin.site.register(characters, DatabseSearchAdmin)
from .models import database_search

class DatabseSearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(database_search, DatabseSearchAdmin)
