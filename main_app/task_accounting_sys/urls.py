from django.urls import path

from .views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView, BoundTasks

app_name = "tasks"

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('bound/', BoundTasks.as_view(), name='bound_list'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
]
