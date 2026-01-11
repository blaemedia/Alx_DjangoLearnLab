# Create Operation

## Description
This document demonstrates how to create a new `Book` instance using the Django shell.

## Command Used
```python
from bookshelf.models import Book
book = Book.objects.create(
    title="Things Fall Apart",
    author="Chinua Achebe",
    publication_year=1958
)
book
