from rest_framework.generics import ListAPIView

from app.models import TestDescription
from app.serializers import TestDescriptionListSerializer


class TestDescriptionListAPIView(ListAPIView):
    def get_queryset(self):
        return TestDescription.objects.all()

    def get_serializer_class(self):
        return TestDescriptionListSerializer
