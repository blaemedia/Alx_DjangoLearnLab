# Retrieve Operation

## Description
This document demonstrates how to retrieve an existing `Book` record from the database using the Django shell.

## Command Used
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book
