# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
# from rest_framework_simplejwt import tokens

# client = APIClient()
# client.post('/notes/', {'title': 'new idea'}, format='json')

#
# class RegisterTestCase(APITestCase):
#
#     def setUp(self) -> None:
#         self.user = User.objects.create(username='user', password='useruser')
#
#     def test_register(self):
#         data = {
#             "username": "test_case",
#             "password": "test_case",
#         }
#         response = self.client.post(reverse('authentication:register'), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         response = self.client.post(reverse('authentication:register'), data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_token(self):
#         pass
#     """lesson 63"""
