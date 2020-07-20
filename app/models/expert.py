from django.db import models
from django.contrib.auth.models import User


class Expert(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )

    laboratory = models.ForeignKey(
        to='app.Laboratory',
        on_delete=models.CASCADE,
    )
