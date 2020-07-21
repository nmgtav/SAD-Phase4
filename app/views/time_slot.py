from django.http import JsonResponse
from rest_framework.views import APIView

from app.controller import TestRequestHandler


class TimeSlotListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        time_slots_list = TestRequestHandler.get_time_slots(self.request.query_params.get('lab'))
        return JsonResponse(
            data=time_slots_list,
            status=200,
            safe=False,
        )
