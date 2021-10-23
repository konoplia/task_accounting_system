from django.urls import path

from .views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView, BoundTasks


app_name = "tasks"

urlpatterns = [
    path('tasks/bound/', BoundTasks.as_view()),
    path('tasks/', TaskListView.as_view()),
    path('tasks/create/', TaskCreateView.as_view()),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view()),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view()),
]
