from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.

    Includes custom validation to ensure publication_year
    is not in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Field-level validation:
        Ensures the publication year is not greater
        than the current year.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model.

    Includes nested serialization of related books.
    The 'books' field comes from the related_name in the Book model.
    read_only=True ensures books are retrieved but not created here.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
