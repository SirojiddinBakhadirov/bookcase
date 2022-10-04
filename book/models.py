from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    STATUS = (
        (1, 'new'),
        (2, 'reading'),
        (3, 'finished')
    )
    status = models.CharField(max_length=200, choices=STATUS)
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    writing_year = models.DateField()
    pages = models.IntegerField()