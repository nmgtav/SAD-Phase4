import random

from app.models import LabTest


class Insurance:
    # This class should get the price based on the test, the laboratory and the insurance of the patient.
    @staticmethod
    def get_price(test, patient):
        return random.randrange(200000, 1000000, 10000)
