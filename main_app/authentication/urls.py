from django.urls import path, include
from .views import RegisterView, LoginView

urlpatterns = [
    path('', RegisterView.as_view()),
    path('login', LoginView.as_view()),

]
