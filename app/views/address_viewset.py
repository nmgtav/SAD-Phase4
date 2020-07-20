from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from app.models import Address
from app.serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    def get_queryset(self):
        return Address.objects.filter(patient_id=1)

    def get_serializer_class(self):
        return AddressSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        data['patient_id'] = 1
        address = Address.objects.create(
            **data
        )
        return JsonResponse(
            data={
                'id': address.id
            },
            status=200,
        )
