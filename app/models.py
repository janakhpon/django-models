from django.db import models

class User(models.Model):
    """User model"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email
