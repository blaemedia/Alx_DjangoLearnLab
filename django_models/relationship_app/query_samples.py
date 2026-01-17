# query_samples.py
import os
import django

# Setup Django environment so we can use models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Alx_DjangoLearnLab.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# 1. Query all books by a specific author
# -----------------------------
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # related_name='books' in Book model
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

# -----------------------------
# 2. List all books in a library
# -----------------------------
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # ManyToManyField
        print(f"Books in {library.name}:")
        for book in books:
            print(f"- {book.title} (Author: {book.author.name})")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

# -----------------------------
# 3. Retrieve the librarian for a library
# -----------------------------
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # OneToOneField related_name
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")

# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    books_by_author("J.K. Rowling")
    print("\n")
    books_in_library("Central Library")
    print("\n")
    librarian_for_library("Central Library")
