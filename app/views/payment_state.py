from rest_framework.views import APIView

from app.models import Payment


class PaymentStateAPIView(APIView):

    def patch(self, request, *args, **kwargs):

        is_successful = self.request.data.get('is_successful')
        payment_id = kwargs.get('pk')
        payment = Payment.objects.get(id=payment_id)
        payment.is_successful = is_successful
        payment.save()
