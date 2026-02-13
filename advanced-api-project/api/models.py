from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Author model represents a book author.

    Fields:
    - name: Stores the author's full name.

    Relationship:
    One Author can have multiple Books (one-to-many).
    The related_name='books' allows reverse lookup:
    author.books.all()
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an Author.

    Fields:
    - title: Title of the book
    - publication_year: Year the book was published
    - author: ForeignKey linking to Author

    Relationship:
    Each Book belongs to one Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
