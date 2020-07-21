from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from app.controller import TestRequestHandler


class PaymentStateAPIView(APIView):

    def patch(self, request, *args, **kwargs):

        is_successful = True if self.request.query_params.get('is_successful') == '1' else False
        payment_id = kwargs.get('pk')
        TestRequestHandler.update_payment_status(payment_id, is_successful)
        return JsonResponse(
            {
                'details': 'payment state updated'
            },
            status=status.HTTP_200_OK
        )
