
---

## 📄 `update.md`

```md
# Update Operation

## Description
This document explains how to update the title of an existing `Book` record.

## Command Used
```python
book = Book.objects.get(id=1)
book.title = "Things Fall Apart (Updated)"
book.save()
book
