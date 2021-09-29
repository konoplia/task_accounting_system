from django.urls import path

from .views import TaskView


app_name = "tasks"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>', TaskView.as_view()),
]
