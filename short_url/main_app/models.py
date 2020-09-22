from django.db import models

# Create your models here.
class Urls(models.Model):
    long_url = models.CharField(max_length=10000)
    short_url = models.CharField(max_length=30)

    def __str__(self):
        return self.long_url
