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
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name



class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowings")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrowings")
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.member.name} - {self.book.title}"