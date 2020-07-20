from django.db import models


class Test(models.Model):
    lab_test = models.ForeignKey(
        to='app.LabTest',
        related_name='tests',
        on_delete=models.CASCADE,
    )

    # Should be connected to the TestResult class too, but as the class is not implemented in this
    # use case, it won't be implemented.

    test_request = models.ForeignKey(
        to='app.TestRequest',
        related_name='tests',
        on_delete=models.CASCADE,
    )
