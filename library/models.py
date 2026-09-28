from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    genre=models.CharField(max_length=50)
    availeble=models.BooleanField(default=True)


    def __str__(self):
        return self.title

class Member(models.Model):
    name=models.CharField(max_length=100)
    borrowed_books=models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name