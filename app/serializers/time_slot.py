from rest_framework import serializers

from app.models import TimeSlot


class TimeSlotListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSlot
        fields = (
            'start_date',
            'end_date',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['expert'] = instance.expert.user.first_name + '-' + instance.expert.user.last_name
        return data
