from django.db import models


class Laboratory(models.Model):

    name = models.CharField(
        max_length=64,
    )
