import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Planet, People
from api.fixtures import SINGLE_PEOPLE_OBJECT, PEOPLE_OBJECTS
from api.serializers import serialize_people_as_json


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
        qs = People.objects.select_related('homeworld').all()
        data = [serialize_people_as_json(people) for people in qs]
    elif request.method == 'POST':
        # POST /people
        planet_id = payload.get('homeworld', None)
        try:
            planet = Planet.objects.get(id=planet_id)
        except Planet.DoesNotExist:
            return JsonResponse(
                {"success": False, "msg": "Could not find planet with id: {}".format(planet_id)},
                status=404)
        try:
            people = People.objects.create(
                name=payload['name'],
                homeworld=planet,
                height=payload['height'],
                mass=payload['mass'],
                hair_color=payload['hair_color'])
        except (ValueError, KeyError):
            return JsonResponse(
                {"success": False, "msg": "Provided payload is not valid"},
                status=400)
        data = serialize_people_as_json(people)
        status = 201
    else:
        data = {"success": False, "msg": "Invalid HTTP method"}
        status=400

    return JsonResponse(data, status=status, safe=False)


@csrf_exempt
def people_detail_view(request, people_id):
    try:
        people = People.objects.get(id=people_id)
    except People.DoesNotExist:
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
        data = serialize_people_as_json(people)
    elif request.method in ['PUT', 'PATCH']:
        # PUT/PATCH /people/:id
        for field in ['name', 'homeworld', 'height', 'mass', 'hair_color']:
            if not field in payload:
                if request.method == 'PATCH':
                    continue
                return JsonResponse(
                    {"success": False, "msg": "Missing field in full update"},
                    status=400)

            if field == 'homeworld':
                try:
                    payload['homeworld'] = Planet.objects.get(id=payload['homeworld'])
                except Planet.DoesNotExist:
                    return JsonResponse(
                        {"success": False, "msg": "Could not find planet with id: {}".format(payload['homeworld'])},
                        status=404)
            try:
                setattr(people, field, payload[field])
                people.save()
            except ValueError:
                return JsonResponse(
                    {"success": False, "msg": "Provided payload is not valid"},
                    status=400)
        data = serialize_people_as_json(people)
    elif request.method == 'DELETE':
        # DELETE /people/:id
        people.delete()
        data = {"success": True}
    else:
        data = {"success": False, "msg": "Invalid HTTP method"}
        status=400

    return JsonResponse(data, status=status, safe=False)
