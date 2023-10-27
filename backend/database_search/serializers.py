from rest_framework import serializers
# from .models import characters
from .models import database_search

class Database_searchSerializer(serializers.ModelSerializer):
    class Meta:
        # model = characters
        # fields = ('Name', 'ChapterReveal', 'EpisodeReveal', 'YearReveal', 'Notes' )

        model = database_search
        fields = ('id', 'title', 'description', 'completed')
