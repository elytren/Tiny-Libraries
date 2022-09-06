from django.db import models

# Create your models here.

class Library(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.title


