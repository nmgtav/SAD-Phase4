import uuid

from django.db import models


class TestDescription(models.Model):
    name = models.CharField(
        max_length=30,
    )
