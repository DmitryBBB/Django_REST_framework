from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    region = models.TextChoices('RU', 'EU')
    birth_day = models.DateField()

