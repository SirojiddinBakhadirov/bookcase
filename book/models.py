from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=200)


class Shelf(models.Model):
    STATUS = (
        (1, 'new'),
        (2, 'reading'),
        (3, 'finished')
    )
    status = models.CharField(max_length=200, choices=STATUS)
    book_name = models.CharField(max_length=200)
    book_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    book_author = models.CharField(max_length=200)
    book_writing_year = models.DateField()
    book_pages = models.IntegerField()
