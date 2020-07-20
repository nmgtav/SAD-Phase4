from rest_framework import serializers

from app.models import TestDescription


class TestDescriptionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestDescription
        fields = (
            'name',
            'id'
        )
