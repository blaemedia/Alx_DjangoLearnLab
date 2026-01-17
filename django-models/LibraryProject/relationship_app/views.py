# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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



@login_required
def home_view(request):
    return render(request, "relationship_app/home.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {username}!")
                return redirect("home")  # Redirect to your homepage or dashboard
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, "relationship_app/logout.html")