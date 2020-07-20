from django.db import models
from app.models import TimeSlot, Patient, Address


class Appointment(models.Model):

    time_slot = models.ForeignKey(
        to=TimeSlot,
        on_delete=models.CASCADE,
    )

    patient = models.ForeignKey(
        to=Patient,
        on_delete=models.CASCADE,
    )

    address = models.ForeignKey(
        to=Address,
        on_delete=models.CASCADE,
    )
