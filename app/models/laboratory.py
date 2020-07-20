from django.db import models


class Laboratory(models.Model):

    name = models.CharField(
        max_length=64,
    )

    def get_available_tests(self):
        return self.tests.filter(available=True)
