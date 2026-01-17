# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# -----------------------------
# Function-Based View: List all books
# -----------------------------
def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

# -----------------------------
# Class-Based View: Display library details
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Include books in the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
