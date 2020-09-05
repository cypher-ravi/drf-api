from django.http import JsonResponse
from django.shortcuts import render


#third party imports
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
        'name': 'Ravi',
        'age' : 20
        }
        return Response(data)


# Create your views here.
# def test_view(request):
    # data = {
    #     'name': 'Ravi',
    #     'age' : 20
    # }
#     return JsonResponse(data, safe=False)