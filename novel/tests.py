from django.test import TestCase

# Create your tests here.
from . import models
class Test1(TestCase):
    def setUp(self):
        pass
    def test_book(self):
        book = models.BookInfo(book_name="1")
        chapter1 = models.BookChapter(book_id=book, name="1")
        chapter2 = models.BookChapter(book_id=book, name="2")
        book.save()
        chapter1.save()
        chapter2.save()
        print(book.bookchapter_set.filter(name="1").values())
        self.assertEqual(1, 1)

