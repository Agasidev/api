from django.urls import path
from .views import BookListView, BookDetailView, BookDetailSlugView

urlpatterns = [
    path('book/', BookListView.as_view(), name = 'book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/<slug:slug>/', BookDetailSlugView.as_view(), name = 'book-detail-slug')
]
