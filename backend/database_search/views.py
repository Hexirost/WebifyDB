from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Database_searchSerializer
from .models import characters
# from .models import database_search

# Create your views here.

class Database_searchView(viewsets.ModelViewSet):
    serializer_class = Database_searchSerializer
    queryset = characters.objects.all()
    # queryset = database_search.objects.all()