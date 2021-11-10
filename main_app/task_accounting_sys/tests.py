from django.contrib.auth.models import User, Group
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from datetime import timedelta

from .models import Task

from .tasks import delete_exp_task


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
        self.creator = User.objects.create_user(username="creator", password="example@123")
        self.user = User.objects.create_user(username="example", password="example@123")
        self.token = AccessToken.for_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer' + ' ' + str(self.token))
        self.task = Task.objects.create(created_by=self.creator, name="test task", description="test description")

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

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TaskManagerGroupMemberTestCase(APITestCase):

    def setUp(self) -> None:
        self.manager = User.objects.create_user(username="example", password="example@123")
        manager_group = Group.objects.create(name='Managers')
        self.manager.groups.add(manager_group)
        self.token = AccessToken.for_user(user=self.manager)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        self.task_manager = Task.objects.create(created_by=self.manager, name="test task", description="test description")
        self.task1_manager = Task.objects.create(created_by=self.manager, name="test task", description="test description")

        self.another_manager = User.objects.create_user(username="example1", password="example@123")
        self.another_manager.groups.add(manager_group)
        self.task_another_manager = Task.objects.create(created_by=self.another_manager, name="test task", description="test description")

        self.developer = User.objects.create_user(username="example2", password="example@123")
        developer_group = Group.objects.create(name='Developers')
        self.developer.groups.add(developer_group)
        self.token = AccessToken.for_user(user=self.developer)

    def test_manager_list_task(self):
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Task.objects.all()))

    def test_manager_bound_list_task(self):
        response = self.client.get(reverse('tasks:bound_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Task.objects.filter(created_by=self.manager.id)))

    def test_manager_create_task(self):
        data = {
            "name": "test task",
            "description": "just test task"
        }

        response = self.client.post(reverse('tasks:create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_manager_create_task_with_wrong_field(self):
        data = {
            "wrong field": 1
        }

        response = self.client.post(reverse('tasks:create'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_manager_create_task_assign_to_himself(self):
        data = {
            "name": "test task",
            "description": "just test task",
            "executor": self.manager.id
        }
        response = self.client.post(reverse('tasks:create'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_manager_update_task(self):
        data = {
            "status": '2_READY'
        }

        response1 = self.client.put(reverse('tasks:update', args=(self.task_manager.id,)), data)
        response2 = self.client.put(reverse('tasks:update', args=(self.task_another_manager.id,)), data)
        response3 = self.client.delete(reverse('tasks:delete', args=((Task.objects.last().id + 1),)))
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response3.status_code, status.HTTP_404_NOT_FOUND)

    def test_manager_update_task_with_wrong_field(self):
        data = {
            "wrong_field": "test"
        }

        response = self.client.put(reverse('tasks:update', args=(self.task_manager.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_manager_delete_task(self):
        response = self.client.delete(reverse('tasks:delete', args=(self.task_manager.id,)))
        response1 = self.client.delete(reverse('tasks:delete', args=(self.task_another_manager.id,)))
        response2 = self.client.delete(reverse('tasks:delete', args=((Task.objects.last().id+1),)))
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        self.assertEqual(response1.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)


class TaskDeveloperGroupMemberTestCase(APITestCase):

    def setUp(self) -> None:
        self.developer = User.objects.create_user(username="example2", password="example@123")
        developer_group = Group.objects.create(name='Developers')
        self.developer.groups.add(developer_group)
        self.token = AccessToken.for_user(user=self.developer)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))

        self.user = User.objects.create_user(username="example1", password="example@123")
        self.task = Task.objects.create(created_by=self.user, name="test task1", description="test description1")
        self.task1 = Task.objects.create(created_by=self.user, name="test task2", description="test description2", executor=self.developer)
        self.task2 = Task.objects.create(created_by=self.user, name="test task3", description="test description3", executor=self.developer, status=2)

    def test_developer_list_task(self):
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Task.objects.all()))

    def test_developer_bound_list_task(self):
        response = self.client.get(reverse('tasks:bound_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Task.objects.filter(executor=self.developer.id)))

    def test_developer_create_task(self):
        response = self.client.post(reverse('tasks:create'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_developer_update_task(self):
        data = {
            "status": '2_READY'
        }
        response = self.client.put(reverse('tasks:update', args=(self.task.id,)), data)
        response1 = self.client.put(reverse('tasks:update', args=(self.task1.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_developer_update_task_with_wrong_field(self):
        data = {
            "non field": 231
        }
        response = self.client.put(reverse('tasks:update', args=(self.task.id,)), data)
        response1 = self.client.put(reverse('tasks:update', args=(self.task1.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)

    def test_developer_delete_task(self):
        response = self.client.delete(reverse('tasks:delete', args=(self.task.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TaskDeleteExpiredTask(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example1", password="example@123")
        self.old_task = Task.objects.create(
            created_by=self.user,
            name="test task3",
            description="test description3",
            life_time=5,
        )

        self.old_task.create_date -= timedelta(days=self.old_task.life_time)
        self.old_task.save()
        delete_exp_task()

    def test_delete_exp_task(self):
        self.assertEqual(len(Task.objects.all()), 0)

