from django.contrib import admin
from django.urls import path, include

from training import views


urlpatterns = [
    # content types
    path('text', views.text_response),
    path('looks-like-json', views.looks_like_json_response),
    path('simple-json', views.simple_json_response),
    path('json', views.json_response),
    path('json-list', views.json_list_response),

    # status codes
    path('json-error', views.json_error_response),

    # methods
    path('only-post', views.only_post_request),
    path('post-payload', views.post_payload),

    # headers
    path('custom-headers', views.custom_headers),

    # URL arguments and parameters
    path('arguments/<int:first_arg>/', views.url_int_argument),
    path('arguments/<str:first_arg>/', views.url_str_argument),
    path('arguments/<str:first_arg>/<int:second_arg>/', views.url_multi_arguments),
    path('arguments/', views.get_params),
]
