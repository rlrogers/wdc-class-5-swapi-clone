import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.fixtures import SINGLE_PEOPLE_OBJECT, PEOPLE_OBJECTS


def single_people(request):
    return JsonResponse(SINGLE_PEOPLE_OBJECT)


def list_people(request):
    return JsonResponse(PEOPLE_OBJECTS, safe=False)


@csrf_exempt
def people_list_view(request):
    if request.body:
        try:
            payload = json.loads(request.body)
        except ValueError:
            return JsonResponse(
                {"success": False, "msg": "Provide a valid JSON payload"},
                status=400)

    status = 200
    if request.method == 'GET':
        # GET /people
        data = PEOPLE_OBJECTS
    elif request.method == 'POST':
        # POST /people
        # TODO: perform proper validations
        PEOPLE_OBJECTS.append(payload)
        data = payload
        status = 201
    else:
        data = {"success": False, "msg": "Invalid HTTP method"}
        status=400

    return JsonResponse(data, status=status, safe=False)


@csrf_exempt
def people_detail_view(request, people_id):
    try:
        result = [doc for doc in PEOPLE_OBJECTS
                  if "/{}/".format(people_id) in doc["url"]][0]
    except IndexError:
        return JsonResponse(
            {"success": False, "msg": "Could not find people with id: {}".format(people_id)},
            status=404)

    if request.body:
        try:
            payload = json.loads(request.body)
        except ValueError:
            return JsonResponse(
                {"success": False, "msg": "Provide a valid JSON payload"},
                status=400)

    status = 200
    if request.method == 'GET':
        # GET /people/:id
        data = result
    elif request.method == 'PUT':
        # PUT /people/:id
        # TODO: perform proper validations
        PEOPLE_OBJECTS[PEOPLE_OBJECTS.index(result)] = payload
        data = payload
    elif request.method == 'PATCH':
        # PATCH /people/:id
        index = PEOPLE_OBJECTS.index(result)
        result.update(payload)
        PEOPLE_OBJECTS[index] = result
        data = result
    elif request.method == 'DELETE':
        # DELETE /people/:id
        PEOPLE_OBJECTS.remove(result)
        data = {"success": True}
    else:
        data = {"success": False, "msg": "Invalid HTTP method"}
        status=400

    return JsonResponse(data, status=status, safe=False)
