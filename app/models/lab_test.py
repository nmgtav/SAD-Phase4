from django.db import models
from app.models import Laboratory


class LabTest(models.Model):

    name = models.CharField(
        max_length=64,
    )

    available = models.BooleanField(
        default=True,
    )

    lab = models.ForeignKey(
        to=Laboratory,
        on_delete=models.CASCADE,
        related_name='tests'
    )
