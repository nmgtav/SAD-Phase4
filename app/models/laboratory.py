from django.db import models


class Laboratory(models.Model):

    name = models.CharField(
        max_length=64,
    )

    def has_every_test(self, tests):
        for test_id in tests:
            if not self.tests.filter(test_description_id=test_id, available=True).exists():
                return False
        return True

    def get_list_of_time_slots(self):
        result = []
        for expert in self.expert_set.all():
            result.extend(list(expert.get_list_of_time_slots()))
        return result
