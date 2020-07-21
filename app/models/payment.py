from django.db import models


class Payment(models.Model):

    amount = models.PositiveIntegerField()

    is_successful = models.NullBooleanField(
        blank=True,
        null=True,
    )

    url = models.URLField(
        max_length=200,
        null=True,
    )

    def update_state(self, success):
        self.is_successful = success
        self.save()

    def get_url(self):
        return self.url.format(payment_pk=self.id)
