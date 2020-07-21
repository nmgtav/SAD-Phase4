from app.models import Payment


class PaymentHandler:
    @staticmethod
    def create_new_payment_request(cost):
        # Sends a request to the Bank Gateway and gets the url which the user should be redirected to.
        # Which then redirects the user to the callback API given to the bank.
        return Payment.objects.create(
            amount=cost,
            url='http://127.0.0.1:8000/api/payment-state/{payment_pk}/',
            is_successful=None,
        )
