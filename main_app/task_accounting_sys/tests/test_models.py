from django.test import TestCase
from ..models import Task
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()


class ModelsTestCase(TestCase):

    @classmethod
    def setUp(cls):
        user = User.objects.create(username='username', password='password')
        self.name = 'test task'




