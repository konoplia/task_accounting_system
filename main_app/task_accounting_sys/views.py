from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import filters

from .models import Task
from .serializers import TaskSerializer

# Create your views here.

FILTERS = [
    'id', 'status', 'priority', 'create_date'
]


class TaskView(ListAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'status', 'priority', 'create_date']

    def post(self, request):
        task = request.data.get('tasks')
        serializer = TaskSerializer(data=task)
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
        return Response({"success": "Task '{}' created successfully".format(task_saved.name)})

    def put(self, request, pk):
        saved_task = get_object_or_404(Task.objects.all(), pk=pk)
        data = request.data.get('tasks')
        serializer = TaskSerializer(instance=saved_task, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
        return Response({
            "success": "Task '{}' updated successfully".format(task_saved.name)
        })

    def delete(self, request, pk):
        task = get_object_or_404(Task.objects.all(), pk=pk)
        task.delete()
        return Response({
            "message": "Task with id `{}` has been deleted.".format(pk)
        }, status=204)
