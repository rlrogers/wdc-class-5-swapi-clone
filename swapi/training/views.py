import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def text_response(request):
    """
    Return a HttpResponse with a simple text message.
    Check that the default content type of the response must be "text/html".
    """
    return HttpResponse('Hello World! This is not a JSON')


def looks_like_json_response(request):
    """
    Return a HttpResponse with a text message containing something that looks
    like a JSON document, but it's just "text/html".
    """
    return HttpResponse('{"name": "Luke Skywalker"}')


def simple_json_response(request):
    """
    Return an actual JSON response by setting the `content_type` of the HttpResponse
    object manually.
    """
    return HttpResponse(
        '{"name": "Luke Skywalker"}',
        content_type='application/json')


def json_response(request):
    """
    Return the same JSON document, but now using a JsonResponse instead.
    """
    new_dict = {"name": "Luke Skywalker"}
    return JsonResponse(new_dict)


def json_list_response(request):
    """
    Return a JsonReponse that contains a list of JSON documents
    instead of a single one.
    Note that you will need to pass an extra `safe=False` parameter to
    the JsonResponse object it order to avoid built-in validation.
    https://docs.djangoproject.com/en/2.0/ref/request-response/#jsonresponse-objects
    """
    new_list = [
        {"name": "Luke Skywalker"},
        {"name": "R2-D2"},
    ]
    return JsonResponse(new_list, safe=False)


def json_error_response(request):
    """
    Return a JsonResponse with an error message and 400 (Bad Request) status code.
    """
    new_dict = {"success": False, "error": "Something went wrong"}
    return JsonResponse(new_dict, status=400)


@csrf_exempt
def only_post_request(request):
    """
    Perform a request method check. If it's a POST request, return a message saying
    everything is OK, and the status code `200`. If it's a different request
    method, return a `400` response with an error message.
    """
    if request.method != 'POST':
        return JsonResponse(
            {"success": False, "msg": "We only allow POST requests"}, status=400)
    return JsonResponse({"success": True, "msg": "Yay! You did it."})


@csrf_exempt
def post_payload(request):
    """
    Write a view that only accepts POST requests, and processes the JSON
    payload available in `request.body` attribute.
    """
    if request.method != 'POST':
        return JsonResponse(
            {"success": False, "msg": "We only support POST requests"}, status=400)

    try:
        payload = json.loads(request.body)
    except ValueError:
        return JsonResponse(
            {"success": False, "msg": "Provide a valid JSON payload"}, status=400)

    if not payload:
        msg = "We got no payload :-("
    else:
        msg = "Yay! We got your payload: {}".format(dict(payload))
    return JsonResponse({"success": True, "msg": msg})


def custom_headers(request):
    """
    Return a JsonResponse and add a custom header to it.
    """
    response = JsonResponse({"success": True})
    response['X-RMOTR-IS-AWESOME'] = True
    return response


def url_int_argument(request, first_arg):
    """
    Write a view that receives one integer parameter in the URL, and displays it
    in the response text.
    """
    return JsonResponse(
        {"success": True, "msg": "We received this argument: {}".format(first_arg)})


def url_str_argument(request, first_arg):
    """
    Write a view that receives one string parameter in the URL, and displays it
    in the response text.
    """
    return JsonResponse(
        {"success": True, "msg": "We received this argument: {}".format(first_arg)})


def url_multi_arguments(request, first_arg, second_arg):
    """
    Write a view that receives two parameters in the URL, and display them
    in the response text.
    """
    return JsonResponse(
        {"success": True, "msg": "We received this two arguments: {}, {}".format(first_arg, second_arg)})


def get_params(request):
    """
    Write a view that receives GET arguments and display them in the
    response text.
    """
    arguments = request.GET
    if not arguments:
        msg = "We got no arguments :-("
    else:
        msg = "Yay! We got your arguments: {}".format(dict(arguments))
    return JsonResponse({"success": True, "msg": msg})
