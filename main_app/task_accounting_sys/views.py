import logging
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import filters

from .models import Task
from .serializers import TaskSerializer, TaskUpdateSerializer

from .permissions import IsOwner, IsManagersGroupMemberOrExecutor, IsManagersGroupMember

# Create your views here.
# logger = logging.getLogger('debug')


class TaskListView(ListAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'status', 'priority', 'create_date']


class TaskCreateView(CreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = (IsManagersGroupMember, )

    def post(self, request):
        # logger.debug(request.data)
        task = request.data
        task['created_by'] = request.user.id
        serializer = TaskSerializer(data=task)
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
        return Response({"success": "Task '{}' created successfully".format(task_saved.name)})


class TaskUpdateView(UpdateAPIView):

    # serializer_class = TaskSerializer
    serializer_class = TaskUpdateSerializer
    permission_classes = (IsManagersGroupMemberOrExecutor,)

    def put(self, request, pk):

        obj = Task.objects.get(id=pk)
        self.check_object_permissions(request, obj)

        saved_task = get_object_or_404(Task.objects.all(), pk=pk)
        data = request.data
        # if request.user.groups.filter(name='Managers').exists():
        print(data)
        serializer = TaskUpdateSerializer(instance=saved_task, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
        return Response({
            "success": "Task '{}' updated successfully".format(task_saved.name)
        })


class TaskDeleteView(DestroyAPIView):

    serializer_class = TaskSerializer
    permission_classes = (IsOwner, )

    def delete(self, request, pk):
        obj = Task.objects.get(id=pk)
        self.check_object_permissions(request, obj)

        task = get_object_or_404(Task.objects.all(), pk=pk)
        task.delete()
        return Response({
            "message": "Task with id `{}` has been deleted.".format(pk)
        }, status=204)
