from django.db import models
from app.models import Expert


class TimeSlot(models.Model):

    expert = models.ForeignKey(
        to=Expert,
        on_delete=models.CASCADE,
    )

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    is_taken = models.BooleanField(
        default=False,
    )
