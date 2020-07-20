from django.db import models
from app.models import Laboratory


class LabTest(models.Model):

    name = models.CharField(
        max_length=64,
    )

    available = models.BooleanField()

    lab = models.ForeignKey(
        to=Laboratory,
        related_name='tests'
    )


    
    

