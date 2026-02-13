# /api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book
import datetime

class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.
    Covers CRUD operations, permissions, filtering, searching, and ordering.
    """

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create sample books
        self.book1 = Book.objects.create(
            title='Python Basics',
            author='Alice',
            published_date=datetime.date(2020, 1, 1),
            isbn='1234567890123'
        )
        self.book2 = Book.objects.create(
            title='Advanced Python',
            author='Bob',
            published_date=datetime.date(2021, 6, 15),
            isbn='9876543210987'
        )

        # URL helpers
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.update_url = lambda pk: reverse('book-update', args=[pk])
        self.delete_url = lambda pk: reverse('book-delete', args=[pk])

    # --- CRUD TESTS ---

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Python Basics')

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        data = {
            'title': 'New Book',
            'author': 'Charlie',
            'published_date': '2022-05-01',
            'isbn': '1112223334445'
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'Unauthorized Book',
            'author': 'Hacker',
            'published_date': '2022-05-01',
            'isbn': '5556667778889'
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username='testuser', password='password123')
        data = {'title': 'Python Basics Updated', 'author': 'Alice', 'published_date': '2020-01-01', 'isbn': '1234567890123'}
        response = self.client.put(self.update_url(self.book1.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Python Basics Updated')

    def test_delete_book(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.delete_url(self.book2.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    # --- FILTERING, SEARCHING, ORDERING TESTS ---

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + '?author=Alice')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Alice')

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + '?search=Advanced')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Advanced Python')

    def test_order_books_by_published_date_desc(self):
        response = self.client.get(self.list_url + '?ordering=-published_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['published_date'], '2021-06-15')
