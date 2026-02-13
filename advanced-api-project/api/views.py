from rest_framework import generics,filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# api/views.py



class BookListView(generics.ListAPIView):
    """
    GET /books/
    Returns a list of all books with advanced query capabilities:
    - Filtering: filter by title, author, or published_date
    - Search: search in title and author fields
    - Ordering: order by any field, default ordering by title
    Permission: Read-only for unauthenticated users, write for authenticated
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filters, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields users can filter by
    filterset_fields = ['title', 'author', 'published_date']

    # Fields users can search in
    search_fields = ['title', 'author']

    # Fields users can order by
    ordering_fields = ['title', 'published_date', 'author']

    # Default ordering
    ordering = ['title']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
