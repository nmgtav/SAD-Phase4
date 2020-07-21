from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from app.controller import TestRequestHandler


class TestRequestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        data['patient'] = 1

        result = TestRequestHandler.create_test_request(data)
        return JsonResponse(
            data={
                    'payment_redirect_url': result.get('payment_url'),
                    'price': result.get('cost')
                 },
            status=status.HTTP_200_OK
        )
