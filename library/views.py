from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_fields = '__all__'
    ordering = ['published_date']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field='id'

class BookDetailSlugView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field='slug'
