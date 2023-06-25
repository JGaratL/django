# import unittest
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User as DjangoUser
from rest_framework.authtoken.models import Token


class GroupCreationTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_group_creation(self):
        data = {'name': 'Group TEST'}
        res = self.client.post('/api_view/group/', data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_user_creation_no_authorized(self):
        self.client.force_authenticate(user=None)
        data = {'group': 'TEST'}
        res = self.client.post('/api_view/group/', data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class GroupListTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_group_list(self):
        res = self.client.get('/api_view/groups/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_group_list_no_authorized(self):
        self.client.force_authenticate(user=None)
        res = self.client.get('/api_view/groups/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

class PersonListTestCase(APITestCase):
    def setUp(self):
        self.user = DjangoUser.objects.create_superuser(username='test', password='test')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_person_list(self):
        res = self.client.get('/api_view/persons/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_group_list_no_authorized(self):
        self.client.force_authenticate(user=None)
        res = self.client.get('/api_view/groups/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
