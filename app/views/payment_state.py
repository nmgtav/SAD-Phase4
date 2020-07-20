from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Payment


class PaymentStateAPIView(APIView):

    def patch(self, request, *args, **kwargs):

        is_successful = True if self.request.query_params.get('is_successful') == '1' else False
        payment_id = kwargs.get('pk')
        payment = Payment.objects.get(id=payment_id)
        payment.is_successful = is_successful
        payment.save()

        return Response('payment state updated', status=status.HTTP_200_OK)