from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from app.controller import TestRequestHandler
from app.models import Address, Patient
from app.serializers import AddressSerializer


class AddressViewSet(ViewSet):

    def get(self, request, *args, **kwargs):
        patient = Patient.objects.get(id=1)
        list_of_addresses = TestRequestHandler.get_list_of_addresses(patient)
        return JsonResponse(
            data=list_of_addresses,
            status=200,
            safe=False,
        )

    def post(self, request, *args, **kwargs):
        data = request.data
        data['patient_id'] = 1
        new_address_id = TestRequestHandler.create_new_address(data)
        return JsonResponse(
            data={'id': new_address_id},
            status=200,
        )