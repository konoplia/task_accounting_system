from django.urls import path

from .views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView


app_name = "tasks"

urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('tasks/create/', TaskCreateView.as_view()),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view()),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view()),
]
