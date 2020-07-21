from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from app.controller import TestRequestHandler


class LabsAndPricesAPIView(APIView):

    def get(self, request, *args, **kwargs):
        test_ids = self.request.query_params.get('tests', [])

        if test_ids:
            test_ids = list(test_ids.split(','))
        data = TestRequestHandler.get_labs_and_prices(test_ids, patient_id=1)
        return JsonResponse(status=status.HTTP_200_OK, data=data, safe=False)
