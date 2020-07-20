from django.db import models


class TestRequest(models.Model):
    payment_request = models.OneToOneField(
        to='app.Payment',
        related_name='test_request',
        on_delete=models.CASCADE,
    )

    appointment = models.OneToOneField(
        to='app.Appointment',
        related_name='test_request',
        on_delete=models.CASCADE,
    )
