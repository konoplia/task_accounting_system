from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import Group

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from .models import Task
from .serializers import TaskSerializer, TaskDeveloperSerializer, TaskManagerSerializer


class TaskUnauthorizedUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="example@123")
        self.task = Task.objects.create(created_by=self.user, name="test task", description="test description")

    def test_unauthorized_create_task(self):
        data = {
            "name": "test task",
            "description": "just test task"
        }
        response = self.client.post(reverse('tasks:create'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_list_task(self):
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_bound_list_task(self):
        response = self.client.get(reverse('tasks:bound_list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_update_task(self):
        response = self.client.put(reverse('tasks:update', args=(self.task.id,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthorized_delete_task(self):
        response = self.client.delete(reverse('tasks:delete', args=(self.task.id,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TaskAuthorizedUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="example@123")
        self.token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer' + ' ' + str(self.token))
        self.task = Task.objects.create(created_by=self.user, name="test task", description="test description")

    def test_authorized_list_task(self):
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorized_bound_list_task(self):
        response = self.client.get(reverse('tasks:bound_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorized_create_task(self):
        data = {
            "name": "test task",
            "description": "just test task"
        }
        response = self.client.post(reverse('tasks:create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_update_task(self):
        response = self.client.put(reverse('tasks:update', args=(self.task.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_delete_task(self):
        response = self.client.delete(reverse('tasks:delete', args=(self.task.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TaskManagerGroupMemberTestCase(APITestCase):

    def setUp(self) -> None:
        manager_group = Group.objects.create(name='Managers')
        self.user = User.objects.create_user(username="example", password="example@123")
        self.user.groups.add(manager_group)
        self.token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer' + ' ' + str(self.token))

    def test_manager_create_task(self):
        data = {
            "name": "test task",
            "description": "just test task"
        }

        response = self.client.post(reverse('tasks:create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
