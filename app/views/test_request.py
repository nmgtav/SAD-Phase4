from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.controller import TestRequestHandler
from app.models import TestRequest, Patient, Laboratory, TimeSlot, Address, Appointment, Payment, Test
from app.insurance_checker import Insurance


class TestRequestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        data['patient'] = 1

        result = TestRequestHandler.create_test_request(data)
        return Response(
            data={
                    'payment_redirect_url': 'http://127.0.0.1:8000/api/payment-state/{payment_pk}/'.format(
                        payment_pk=result.get('payment_id')
                    ),
                    'price': result.get('cost')
                 },
            status=status.HTTP_200_OK
        )
