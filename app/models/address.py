from django.db import models


class Address(models.Model):
    address = models.TextField()

    patient = models.ForeignKey(
        to='app.Patient',
        related_name='addresses',
        on_delete=models.CASCADE,
    )
