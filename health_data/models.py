from django.db import models
from authentication.models import Student


class HealthRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    temperature = models.FloatField()
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
