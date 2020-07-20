from django.db import models


class LabTest(models.Model):

    name = models.CharField(
        max_length=64,
    )

    available = models.BooleanField(
        default=True,
    )

    lab = models.ForeignKey(
        to='app.Laboratory',
        related_name='tests',
        on_delete=models.CASCADE,
    )

    test_description = models.ForeignKey(
        to='app.TestDescription',
        on_delete=models.CASCADE,
        related_name='lab_tests',
    )