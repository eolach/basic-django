from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rxit.models import Prescriber
from rxit.serializers import PrescriberSerializer

# Create your views here.
@csrf_exempt
def prescriber_list(request):
    if request.method == 'GET':
        prescribers = Prescriber.objects.all()
        serializer = PrescriberSerializer(prescribers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request_method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrescriberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JsonResonse(serializer.errors, status=400)

@csrf_exempt
def prescriber_detail(request, pk):
    """ Retrieve, create, delete a prescriber
    """
    try:
        prescriber = Prescribers.objects.get(pk=pk)
    except Prescriber.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PrescriberSerializer(prescriber)
        return HttpResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrescriberSerializer(prescriber, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        prescriber.delete()
        return HttpResponse(status=204)