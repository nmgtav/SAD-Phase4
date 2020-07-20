from rest_framework import serializers

from app.models import TimeSlot


class TimeSlotListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSlot
        fields = (
            'id',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['date'] = str(instance.start_date.date()) + ' ' + instance.start_date.strftime('%H:%M') + '-' + \
                       instance.end_date.strftime('%H:%M')
        return data
