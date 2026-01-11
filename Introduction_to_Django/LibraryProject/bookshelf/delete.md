
---

## 📄 `delete.md`

```md
# Delete Operation

## Description
This document demonstrates how to delete a `Book` record from the database.

## Command Used
```python
book = Book.objects.get(id=1)
book.delete()
