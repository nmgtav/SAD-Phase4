from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from app.models import Laboratory, Patient


class LabsAndPricesAPIView(APIView):

    def get(self, request, *args, **kwargs):
        patient = Patient.objects.get(id=1)
        test_ids = self.request.query_params.get('tests', [])

        if test_ids:
            test_ids = list(test_ids.split(','))

        proper_labs = []
        for lab in Laboratory.objects.all():
            for test_id in test_ids:
                if not lab.tests.filter(test_description_id=test_id).exists():
                    break
            else:
                proper_labs.append(lab)

        data = list()
        for lab in proper_labs:

            data_instance = dict()
            data_instance['id'] = lab.id
            data_instance['name'] = lab.name

            lab_total_cost = 0
            for test_id in test_ids:
                lab_total_cost += insurance_checker.get_price(lab.tests.get(test_description_id=test_id), patient)

            data_instance['price'] = lab_total_cost
            data.append(data_instance)

        return JsonResponse(status=status.HTTP_200_OK, data=data, safe=False)
