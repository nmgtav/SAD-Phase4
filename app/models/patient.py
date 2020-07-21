from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )

    def get_list_of_addresses(self):
        return self.addresses.all()
