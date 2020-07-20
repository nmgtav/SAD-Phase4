from django.db import models


class Appointment(models.Model):

    time_slot = models.ForeignKey(
        to='app.TimeSlot',
        on_delete=models.CASCADE,
    )

    patient = models.ForeignKey(
        to='app.Patient',
        on_delete=models.CASCADE,
    )

    address = models.ForeignKey(
        to='app.Address',
        on_delete=models.CASCADE,
    )
