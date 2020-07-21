from django.db import models


class Appointment(models.Model):

    time_slot = models.ForeignKey(
        to='app.TimeSlot',
        on_delete=models.CASCADE,
    )

    test_request = models.OneToOneField(
        to='app.TestRequest',
        on_delete=models.CASCADE,
        null=True,
    )

    address = models.ForeignKey(
        to='app.Address',
        on_delete=models.CASCADE,
    )

    expert = models.ForeignKey(
        to='app.Expert',
        on_delete=models.CASCADE,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.expert:
            self.expert = self.time_slot.lab.get_suitable_expert(self.address)
        super(Appointment, self).save(*args, **kwargs)
