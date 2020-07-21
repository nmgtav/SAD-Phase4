from app.models import TestDescription


class DAO:
    @staticmethod
    def get_list_of_all_test_descriptions():
        return TestDescription.objects.all()
