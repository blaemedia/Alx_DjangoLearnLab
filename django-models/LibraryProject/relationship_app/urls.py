# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Function-Based View
    path('books/', views.book_list_view, name='book-list'),

    # Class-Based View
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]
