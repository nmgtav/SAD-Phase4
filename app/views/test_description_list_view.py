from django.http import JsonResponse
from rest_framework.views import APIView

from app.controller import TestRequestHandler
from app.initialize import initialize


class TestDescriptionListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        list_of_tests = TestRequestHandler.get_test_descriptions()
        if not list_of_tests:
            initialize()
        return JsonResponse(
            data=list_of_tests,
            status=200,
            safe=False,
        )
