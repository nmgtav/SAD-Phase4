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
        return self.timeslot_set.all()

    def get_test(self, id):
        return self.tests.get(id=id)

    def get_time_slot(self, time_slot_id):
        return self.timeslot_set.get(id=time_slot_id, is_taken=False)

    def get_suitable_expert(self, address):
        from app.models import Expert

        # Should appoint an expert who has vacant time in that interval and is near to the address
        return Expert.objects.get(id=1)
