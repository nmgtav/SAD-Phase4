class PaymentHandler:
    @staticmethod
    def get_payment_url(payment):
        # Sends a request to the Bank Gateway and gets the url which the user should be redirected to.
        # Which then redirects the user to the callback API given to the bank.
        return 'http://127.0.0.1:8000/api/payment-state/{payment_pk}/'.format(payment_pk=payment.id)
