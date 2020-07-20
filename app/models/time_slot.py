from django.db import models


class TimeSlot(models.Model):

    expert = models.ForeignKey(
        to='app.Expert',
        on_delete=models.CASCADE,
    )

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    is_taken = models.BooleanField(
        default=False,
    )
