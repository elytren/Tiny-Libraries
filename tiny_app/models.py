from django.db import models

# Create your models here.

class Library(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    longitude = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title




