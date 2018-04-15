# SWAPI Clone

Do you love Star Wars as much as we do? In order to practice Web Services and RESTful APIs with Django, today we will build a basic Star Wars API using regular Django views and URLs. 💪

We will use the data model provided by this open and free web service: [https://swapi.co/](https://swapi.co/). Check it out and play with it for better understanding of the type of data we will be handling. We will just concentrate in the `/people` endpoint, and its relationship with the `/planets` one.

## Initial RESTful training

### 1) Install a HTTP client

To properly work and test APIs you will need to use a HTTP client app. It will allow you to make GET, POST, DELETE, etc requests to different endpoints, handle headers, content types, parameters, etc. There are many HTTP clients available, but we recommend to work either with [Postman](https://www.getpostman.com/) or [Insomnia](https://insomnia.rest/). You can also test it from the Python terminal using the [requests](http://docs.python-requests.org/en/master/) library, but for this particular use case it won't be very convenient.

When properly installed, the HTTP client (in this case we are using Postman) should look similar to this:

![image](https://user-images.githubusercontent.com/1155573/38784572-339bb930-40ea-11e8-906f-71d6ee07445e.png)

Note that in the top section you have a text input to write the API endpoint you want to request, as well as a drop down to select the HTTP method (GET, POST, etc) you are willing to use. Other sections, like headers or authentication might also be useful for further tasks.

If you have your client up and running, it's time to do our first approach to building an API using Django. 🙌

### 2) Playing with the `training` app

This Django project provides a `tracking` app. The goal of this app is doing an initial practice of how to use Django views to construct the basic structure of a web service. We will learn how to return different content types (JSON, HTML, XML, etc), use the different HTTP methods (GET, POST, etc), handle headers, status codes, and more.

Each function in the `training/views.py` module provides a short explanation of what the view is supposed to do. Just follow the instructions and implement each of them from top to bottom. Once finished, you should have a clearer understanding of how APIs with Django work.

## Cloning SWAPI

Ok, it's time to build something real! 🎉 No more toy exercises, let's work in an actual RESTful API. As we explained before, we want to make a clone of [https://swapi.co/](https://swapi.co/). Not a complete clone, just concentrate in the `/people` endpoint for now (we encourage you to implement other endpoints as well if you have time and will to keep learning).

In the `api/models.py` module we provide you with two small Django Models: `People` and `Planet`. As you can see, there's a `FK` relationship between them. The goal of the practice is to build a whole `CRUD` (create, read, update, delete) web service for these models.

Let's start by differentiating between `list` and `detail` API calls. We say we have a `list` API call when we request information about many objects or perform an action that doesn't affect any object in particular. For example: "give me all the `People` objects in the database", "create a new `People` object". On the other hand, `detail` API calls will concentrate actions in one particular object (with a specific object ID). For example: "give me the `People` object with ID equals to `99`", "update `People` object with ID equal to `100` and set `name="Luke Skywalker"`", "delete object with ID equal to `120`", etc. You get the pattern?

If we combine listing/detailing requests with the different HTTP methods, we get the main concepts behind a RESTful architecture: Actions are defined by given HTTP method, and are applied either on one specific object (detail request), or to the whole set of objects (list requests).
This small table has a summary of what we've been explaining, and might be handy to get a better understanding of how REST works.

![image](https://user-images.githubusercontent.com/1155573/38784732-d5754562-40ec-11e8-8384-e3fa1b7280a7.png)

That said, we will split our functionality in two main views. One for "detail" actions and other for "list" actions. The detail-based view will always receive one `id` parameter, that represents the object we want to apply the action to.

Inside each of the view functions, you should evaluate the content of `request.method` attribute to determine which kind of action you need to perform (read, create, delete, etc).

We encourage you to check the `api/tests.py` module for better understanding of the functionality we are expecting.

The final result of this project should look similar to this:

![image](https://user-images.githubusercontent.com/1155573/38784846-759f3920-40ee-11e8-8916-cef5263bffa1.png)

Note that this screenshot shows the result of a listing request to the `/people` endpoint. The detail of one particular object will look almost the same, but returning one particular JSON document instead of a list of them.

## Final notes

Web services are a key component of today's internet. Either by consuming or creating APIs, you will be constantly in touch with them. That's why it's so important to get accustomed and properly understand how they work.

In this practice we are building our API in the most rudimentary way. That means, without using any library or tools, and manually implementing each of the aspects of it. In the next practice, we will learn how to implement this same API using the wonderful [Django REST Framework](http://www.django-rest-framework.org/) library. Stay tuned 😉
