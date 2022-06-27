import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory
# Create your tests here.
# Test case for Login
# factory = APIRequestFactory()
# response = factory.post('/notes/',{  "username": "vikram1", "password": "123"})
# assert response.status_code == 200
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from testapp.api import views
import pprint
class Test(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.UserListView.as_view()
        self.uri = '/collection/'

    def test_collection_list_success(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

class Test1(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.UserCreateView.as_view()
        self.uri = '/collectioncreate/'

    def test_collection_create_success(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 405,
                         'Expected Response Code 405, received {0} instead.'
                         .format(response.status_code))

class Test2(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.UserCollection.as_view()
        self.uri = '/mycollection/'

    def test_collection_Mycollection_success(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

class Test3(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MovieViewLC.as_view()
        self.uri = '/movies/'

    def test_collection_Mycollection_success(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 401,
                         'Expected Response Code 401, received {0} instead.'
                         .format(response.status_code))


class Test4(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MovieviewRUD.as_view()
        self.uri = '/movies/<uid>/'

    def test_collection_Update_MovieUpdate_success(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 401,
                         'Expected Response Code 401, received {0} instead.'
                         .format(response.status_code))