from rest_framework.generics import ListAPIView

from app.models import TimeSlot
from app.serializers import TimeSlotListSerializer


class TimeSlotListAPIView(ListAPIView):
    def get_queryset(self):
        return TimeSlot.objects.filter(is_taken=False, expert__laboratory_id=self.request.query_params.get('lab'))

    def get_serializer_class(self):
        return TimeSlotListSerializer
