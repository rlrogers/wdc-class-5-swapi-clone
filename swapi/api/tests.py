import json
from copy import deepcopy

from django.test import TestCase

from api.fixtures import SINGLE_PEOPLE_OBJECT, PEOPLE_OBJECTS


class PeopleEndpointTestCase(TestCase):

    def test_detail(self):
        response = self.client.get('/people/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(), SINGLE_PEOPLE_OBJECT)

    def test_list(self):
        response = self.client.get('/people/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(), PEOPLE_OBJECTS)

    def test_create(self):
        payload = deepcopy(SINGLE_PEOPLE_OBJECT)
        payload['name'] = 'New Document'
        payload['url'] = 'http://localhost:8000/people/6/'
        json_payload = json.dumps(payload)

        response = self.client.post(
            '/people/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(), payload)
        self.assertEqual(len(PEOPLE_OBJECTS), 6)

    def test_partial_update(self):
        payload = {"name": "New name"}
        json_payload = json.dumps(payload)

        response = self.client.patch(
            '/people/1/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['name'], 'New name')
        self.assertEqual(PEOPLE_OBJECTS[0]['name'], 'New name')

    def test_full_update(self):
        payload = deepcopy(SINGLE_PEOPLE_OBJECT)
        payload['name'] = 'New name'
        json_payload = json.dumps(payload)

        response = self.client.put(
            '/people/1/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['name'], 'New name')
        self.assertEqual(PEOPLE_OBJECTS[0]['name'], 'New name')

    def test_delete(self):
        count = len(PEOPLE_OBJECTS)
        response = self.client.delete('/people/6/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(), {'success': True})
        self.assertEqual(len(PEOPLE_OBJECTS), count - 1)

    def test_invalid_json(self):
        json_payload = '{"not a valid JSON"}'
        response = self.client.post(
            '/people/', data=json_payload, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(),
                         {'msg': 'Provide a valid JSON payload', 'success': False})

    def test_detail_invalid_method(self):
        response = self.client.post(
            '/people/1/', data='{}', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(),
                         {'msg': 'Invalid HTTP method', 'success': False})

    def test_list_invalid_method(self):
        response = self.client.delete('/people/', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(),
                         {'msg': 'Invalid HTTP method', 'success': False})
