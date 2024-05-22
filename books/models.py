from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
    
    
#database configuration models
# models.py


class DatabaseConfiguration(models.Model):
    name = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    port = models.IntegerField(null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


