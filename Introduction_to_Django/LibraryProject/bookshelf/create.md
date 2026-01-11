# Create Operation

## Description
This document demonstrates how to create a new `Book` instance using the Django shell.

## Command Used
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book
