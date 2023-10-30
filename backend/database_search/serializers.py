from rest_framework import serializers
from .models import characters

class Database_searchSerializer(serializers.ModelSerializer):
    class Meta:
        model = characters
        fields = ('id', 'name', 'chapter_reveal', 'episode_reveal', 'year_reveal', 'notes' )

        # model = database_search
        # fields = ('id', 'title', 'description', 'completed')
