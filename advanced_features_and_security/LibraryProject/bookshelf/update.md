# Update Operation

## Description
This document demonstrates how to update the title of an existing `Book` record using the Django shell.

## Command Used
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
