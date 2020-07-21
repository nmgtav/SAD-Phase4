import uuid

from django.db import models


class TestDescription(models.Model):
    name = models.CharField(
        max_length=30,
    )

    @staticmethod
    def get_list_of_all_test_descriptions():
        return TestDescription.objects.all()