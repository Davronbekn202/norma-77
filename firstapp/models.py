from django.db import models

from accounts.models import CustomUser


class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.full_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
