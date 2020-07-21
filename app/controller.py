from app.models import TestDescription


class TestRequestHandler:
    @staticmethod
    def get_test_descriptions():
        result = []
        for test in TestDescription.get_list_of_all_test_descriptions():
            result.append({'id': test.id, 'name': test.name})
        return result