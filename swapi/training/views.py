from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def text_response(request):
    # simplest response ever. just returning plain text
    return HttpResponse('Hello World! This is not a JSON')


def looks_like_json_response(request):
    # it looks like a JSON response, but it's just text/html content type.
    return HttpResponse('{"name": "Luke Skywalker"}')


def simple_json_response(request):
    # our first JSON response, setting the content type manually
    return HttpResponse(
        '{"name": "Luke Skywalker"}',
        content_type='application/json')


def json_response(request):
    # built-in JsonResponse sets the content type automatically for us
    new_dict = {"name": "Luke Skywalker"}
    return JsonResponse(new_dict)


def json_list_response(request):
    # we can also use a `list` as input of the JsonResponse
    # but we need to disallow `safe` responses
    # https://docs.djangoproject.com/en/2.0/ref/request-response/#jsonresponse-objects
    new_list = [
        {"name": "Luke Skywalker"},
        {"name": "R2-D2"},
    ]
    return JsonResponse(new_list, safe=False)


def json_error_response(request):
    # as JsonResponse is a subclass of HttpResponse, we can override any
    # of its arguments, like `status`
    new_dict = {"success": False, "error": "Something went wrong"}
    return JsonResponse(new_dict, status=400)


@csrf_exempt
def only_post_request(request):
    if request.method != 'POST':
        return JsonResponse(
            {"success": False, "msg": "We only allow POST requests"}, status=400)
    return JsonResponse({"success": True, "msg": "Yay! You did it."})


def custom_headers(request):
    response = JsonResponse({"success": True})
    response['X-RMOTR-IS-AWESOME'] = True
    return response
