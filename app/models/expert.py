from django.db import models
from django.contrib.auth.models import User

from app.models import Laboratory


class Expert(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )

    laboratory = models.ForeignKey(
        to=Laboratory,
        on_delete=models.CASCADE,
    )
