import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.fixtures import SINGLE_PEOPLE_OBJECT, PEOPLE_OBJECTS


def single_people(request):
    return JsonResponse(SINGLE_PEOPLE_OBJECT)


def list_people(request):
    return JsonResponse(PEOPLE_OBJECTS, safe=False)
