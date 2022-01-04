from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    bio = models.TextField(max_length=1000, null = True)
    school = models.CharField(max_length=70)
    college = models.CharField(max_length=70)

    image = models.ImageField(upload_to = "author")

