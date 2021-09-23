# from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer

# Create your views here.


class TaskView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data})

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
        # import pdb
        # pdb.set_trace()
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
        return Response({
            "success": "Task '{}' updated successfully".format(task_saved.name)
        })

    def delete(self, request, pk):
        # Get object with this pk
        task = get_object_or_404(Task.objects.all(), pk=pk)
        task.delete()
        return Response({
            "message": "Task with id `{}` has been deleted.".format(pk)
        }, status=204)
