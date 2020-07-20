from django.db import models
from app.models import TimeSlot, Pat


class Appointment(models.Model):

    time_slot = models.ForeignKey(
        to=TimeSlot,
        on_delete=models.CASCADE,
    )


