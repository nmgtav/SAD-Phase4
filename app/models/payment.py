from django.db import models


class Payment(models.Model):

    amount = models.PositiveIntegerField()

    is_successful = models.BooleanField(
        blank=True,
        null=True,
    )

    def update_state(self, success):
        self.is_successful = success
        self.save()