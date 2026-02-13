from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    List all books with advanced query capabilities.

    Features:
    - Filtering by title, author, and publication_year
    - Search by title and author's name
    - Ordering by title and publication_year
    """

    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer

    # Add DRF filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Fields available for exact filtering
    filterset_fields = ['title', 'publication_year', 'author']

    # Fields available for partial text search
    search_fields = ['title', 'author__name']

    # Fields available for ordering
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']
