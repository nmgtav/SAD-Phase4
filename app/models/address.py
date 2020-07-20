from django.db import models

from app.models import Patient


class Address(models.Model):
    address = models.TextField()

    patient = models.ForeignKey(
        to=Patient,
        related_name='addresses',
        on_delete=models.CASCADE,
    )
