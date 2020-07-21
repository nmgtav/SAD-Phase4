from django.db import models

from app.models import Appointment, Test
from app.payment_handler import PaymentHandler


class TestRequest(models.Model):
    payment_request = models.OneToOneField(
        to='app.Payment',
        related_name='test_request',
        on_delete=models.CASCADE,
        null=True,
    )

    patient = models.OneToOneField(
        to='app.Patient',
        related_name='test_request',
        on_delete=models.CASCADE,
        null=True,
    )

    def get_payment_url(self):
        return self.payment_request.get_url()

    def save(self, *args, **kwargs):
        cost = kwargs.pop('cost', None)
        time_slot = kwargs.pop('time_slot', None)
        address_id=kwargs.pop('address', None)
        test_ids = kwargs.pop('test_ids', None)

        _is_new = not self.pk

        super(TestRequest, self).save(*args, **kwargs)

        if _is_new:
            new_appointment = Appointment(
                address_id=address_id,
                time_slot=time_slot,
                test_request=self,
            )
            new_appointment.save()
            self.appointment = new_appointment

            self.payment_request = PaymentHandler.create_new_payment_request(cost)

            self.save()

            for test in test_ids:
                Test.objects.create(
                    lab_test=self.appointment.time_slot.lab.get_test(test),
                    test_request=self,
                )
