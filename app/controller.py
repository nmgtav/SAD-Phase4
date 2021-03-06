from app.insurance_checker import Insurance
from app.models import (TestDescription, Laboratory, Address, TimeSlot, Patient,
                        Appointment, Payment, TestRequest, Test)
from app.payment_handler import PaymentHandler
from app.dao import DAO


class TestRequestHandler:
    @staticmethod
    def get_test_descriptions():
        result = []
        for test in DAO.get_list_of_all_test_descriptions():
            result.append({'id': test.id, 'name': test.name})
        return result

    @staticmethod
    def get_labs_and_prices(test_ids, patient_id):
        patient = DAO.get_patient(patient_id)
        proper_labs = [lab for lab in DAO.get_list_of_labs() if lab.has_every_test(test_ids)]
        print(proper_labs)
        data = list()
        for lab in proper_labs:

            data_instance = dict()
            data_instance['id'] = lab.id
            data_instance['name'] = lab.name

            lab_total_cost = 0
            for test_id in test_ids:
                lab_total_cost += Insurance.get_price(lab.get_test(test_id), patient)

            data_instance['price'] = lab_total_cost
            data.append(data_instance)
        return data

    @staticmethod
    def get_list_of_addresses(patient_id):
        patient = DAO.get_patient(patient_id)
        address_list = patient.get_list_of_addresses()
        result = []
        for address in address_list:
            result.append({'address': address.address, 'id': address.id})
        return result

    @staticmethod
    def create_new_address(data):
        patient = DAO.get_patient(data.get('patient_id'))
        address_id = patient.create_address(data.get('address'))
        return address_id

    @staticmethod
    def get_time_slots(lab_id):
        lab = DAO.get_laboratory(lab_id)
        time_slots_list = lab.get_list_of_available_time_slots()
        result = []
        print(time_slots_list)
        for time_slot in time_slots_list:
            result.append({
                'id': time_slot.id,
                'date': (
                        str(time_slot.start_date.date()) + ' '
                        + time_slot.start_date.strftime('%H:%M') + '-'
                        + time_slot.end_date.strftime('%H:%M')
                )
            })
        return result

    @staticmethod
    def create_test_request(data):
        patient = DAO.get_patient(data.get('patient'))

        laboratory = DAO.get_laboratory(data.get('laboratory'))

        lab_time_slot = laboratory.get_time_slot(
            data.get('time_slot'),
        )

        test_ids = data.get('tests')

        cost = 0
        for test_id in test_ids:
            cost += Insurance.get_price(laboratory.get_test(id=test_id), patient)

        test_request = TestRequest()
        test_request.save(time_slot=lab_time_slot, cost=cost, address=data.get('address'), test_ids=test_ids)

        payment_url = test_request.get_payment_url()

        return {
            'payment_url': payment_url,
            'cost': cost,
        }

    @staticmethod
    def update_payment_status(payment_id, success):
        payment = Payment.objects.get(id=payment_id)
        payment.update_state(success)
