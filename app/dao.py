from app.models import TestDescription, Laboratory, Patient


class DAO:
    @staticmethod
    def get_list_of_all_test_descriptions():
        return TestDescription.objects.all()

    @staticmethod
    def get_list_of_labs():
        return Laboratory.objects.all()

    @staticmethod
    def get_patient(patient_id):
        return Patient.objects.get(id=patient_id)
