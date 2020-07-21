from django.db import models


class Address(models.Model):
    address = models.TextField()

    patient = models.ForeignKey(
        to='app.Patient',
        related_name='addresses',
        on_delete=models.CASCADE,
    )

    @staticmethod
    def get_list_of_addresses(patient):
        return Address.objects.filter(patient=patient)