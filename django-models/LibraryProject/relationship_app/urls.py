# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Function-Based View
    path('books/', views.book_list_view, name='book-list'),

    # Class-Based View
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),


    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),  # Keep registration as FBV
]

