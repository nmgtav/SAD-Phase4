from app.insurance_checker import Insurance
from app.models import TestDescription, Laboratory, Address


class TestRequestHandler:
    @staticmethod
    def get_test_descriptions():
        result = []
        for test in TestDescription.get_list_of_all_test_descriptions():
            result.append({'id': test.id, 'name': test.name})
        return result

    @staticmethod
    def get_labs_and_prices(test_ids, patient):
        proper_labs = [lab for lab in Laboratory.objects.all() if lab.has_every_test(test_ids   )]

        data = list()
        for lab in proper_labs:

            data_instance = dict()
            data_instance['id'] = lab.id
            data_instance['name'] = lab.name

            lab_total_cost = 0
            for test_id in test_ids:
                lab_total_cost += Insurance.get_price(lab.tests.get(test_description_id=test_id), patient)

            data_instance['price'] = lab_total_cost
            data.append(data_instance)
        return data

    @staticmethod
    def get_list_of_addresses(patient):
        address_list = Address.get_list_of_addresses(patient)
        result = []
        for address in address_list:
            result.append({'address': address.address, 'id': address.id})
        return result

    @staticmethod
    def create_new_address(data):
        address = Address.objects.create(
            **data
        )
        return address.id
