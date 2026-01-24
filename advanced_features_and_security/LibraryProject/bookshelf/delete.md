# Delete Operation

## Description
This document demonstrates how to delete a `Book` record from the database using the Django shell.

## Command Used
```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
