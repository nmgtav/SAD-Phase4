from rest_framework import serializers

from app.models import TimeSlot


class TimeSlotListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSlot
        fields = (
            'start_date',
            'end_date',
            'id',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['laboratory'] = instance.expert.laboratory.name
        return data
