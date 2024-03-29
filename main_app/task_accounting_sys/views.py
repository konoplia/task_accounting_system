from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import filters, status
from .models import Task
from .serializers import TaskSerializer, TaskDeveloperSerializer, TaskManagerSerializer
from .tasks import send_mail_to_executor
# from celery import de

from .permissions import IsOwner, IsManagersGroupMemberAndOwnerOrExecutor, IsManagersGroupMember


class BoundTasks(ListAPIView):
    """
    Returns a list of objects associated with the user.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'status', 'priority', 'create_date']
    ordering = ['id']

    def get_queryset(self):
        if self.request.user.groups.filter(name='Managers').exists():
            queryset = Task.objects.filter(created_by=self.request.user.id)
        else:
            queryset = Task.objects.filter(executor=self.request.user.id)
        return queryset


class TaskListView(ListAPIView):
    """
    Returns the entire list of objects.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'status', 'priority', 'create_date']
    ordering = ['id']


class TaskCreateView(CreateAPIView):
    """
    Accepts two required fields: name and description.
    """

    serializer_class = TaskSerializer
    permission_classes = (IsManagersGroupMember, )

    def post(self, request):
        task = request.data
        serializer = TaskSerializer(data=task, context=request)

        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save(created_by=request.user)

        if task_saved.executor != None:
            send_mail_to_executor.delay(task_saved.id)
        

        return Response({"success": "Task '{}' created successfully".format(task_saved.name)},
                        status=status.HTTP_201_CREATED)


class TaskUpdateView(RetrieveUpdateAPIView):
    """
    Accepts fields and their values ​​depending on access rights.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsManagersGroupMemberAndOwnerOrExecutor,)

    def put(self, request, pk):
        try:
            obj = Task.objects.get(id=pk)
            self.check_object_permissions(request, obj)
        except ObjectDoesNotExist:
            return Response({
                "message": "Task with id `{}` does not exist.".format(pk)
            }, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        saved_task = get_object_or_404(Task.objects.all(), pk=pk)

        if request.user.groups.filter(name='Managers').exists():
            serializer = TaskManagerSerializer(instance=saved_task, data=data, context=request, partial=True)
        else:
            serializer = TaskDeveloperSerializer(instance=saved_task, data=data)

        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()

        return Response({
            "success": "Task '{}' updated successfully".format(task_saved.name)
        })


class TaskDeleteView(DestroyAPIView):
    """
    In case of successful deletion of the object, it returns 205 the server response.
    """

    serializer_class = TaskSerializer
    permission_classes = (IsOwner, )

    def delete(self, request, pk):
        try:
            obj = Task.objects.get(id=pk)
            self.check_object_permissions(request, obj)
        except ObjectDoesNotExist as e:
            return Response({
                "message": "Task with id `{}` does not exist.".format(pk)
            }, status=status.HTTP_404_NOT_FOUND)

        task = get_object_or_404(Task.objects.all(), pk=pk)
        task.delete()
        return Response({
            "message": "Task with id `{}` has been deleted.".format(pk)
        }, status=status.HTTP_205_RESET_CONTENT)

