from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import TestRequest, Patient, Laboratory, TimeSlot, Address, Appointment, Payment, Test
from app.insurance_checker import Insurance


class TestRequestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        patient = Patient.objects.get(
            id=1
        )

        laboratory = Laboratory.objects.get(
            id=self.request.data.get('laboratory')
        )

        lab_time_slot = TimeSlot.objects.get(
            id=self.request.data.get('time_slot'),
            expert__laboratory=laboratory,
            is_taken=False
        )

        address = Address.objects.get(
            id=self.request.data.get('address'),
            patient=patient
        )

        test_ids = self.request.data.get('tests')

        cost = 0
        for test_id in test_ids:
            cost += Insurance.get_price(laboratory.tests.get(test_description_id=test_id), patient)

        appointment = Appointment.objects.create(
            time_slot=lab_time_slot,
            address=address,
            patient=patient,
        )

        payment = Payment.objects.create(
            amount=cost,
            is_successful=False
        )

        test_request = TestRequest.objects.create(
            payment_request=payment,
            appointment=appointment
        )

        for test_id in test_ids:
            Test.objects.create(
                lab_test=laboratory.tests.get(test_description_id=test_id),
                test_request=test_request,
            )

        return Response({
            'payment_redirect_url': '127.0.0.1:8000/api/payment-state/{payment_pk}/?is_successful='.format(
                payment_pk=payment.id
            ),
            'price': cost
        }, status=status.HTTP_200_OK)
