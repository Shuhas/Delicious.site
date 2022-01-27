from django.db import models

# Create your models here.

class Category(models.Model):
    content = models.CharField(max_length=128)
