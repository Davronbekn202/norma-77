from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
