from django.db import models

class Student(models.Model):
    id = models.CharField(max_length=50, unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    gpa = models.DecimalField(decimal_places=2, max_digits=5)
    booksReserved = models.IntegerField(default=0)

class Book(models.Model):
    id = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    currently_checked_out = models.BooleanField()
    number_of_times_checked_out = models.IntegerField(default=0)