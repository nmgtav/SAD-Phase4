from django.db import models
from django.contrib.auth.models import User

from app.models import Address


class Patient(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )

    def get_list_of_addresses(self):
        return self.addresses.all()

    def create_address(self, address):
        new_address = Address.objects.create(
            patient=self,
            address=address,
        )
        return new_address.id
