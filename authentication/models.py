from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="student/")
    photo_embeddings = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        editable=False,
    )
    school = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
