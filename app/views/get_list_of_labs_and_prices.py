from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class GetListOfLabsAndPrices(APIView):

    def get(self, request, *args, **kwargs):

        uids = list(self.request.data.get('uids').split(','))
        print(uids)
        return JsonResponse(status=status.HTTP_200_OK, data={})