import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Book
import unittest
from django.test import Client


class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get('/customer/details/')
        self.assertEqual(response.status_code, 404)

    def test_index(self):
        response = self.client.get('/customer/index/')
        self.assertEqual(response.status_code, 404)
