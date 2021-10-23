import logging

from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import filters

from .models import Task
from .serializers import TaskSerializer, TaskDeveloperSerializer, TaskManagerSerializer

from .permissions import IsOwner, IsManagersGroupMemberAndOwnerOrExecutor, IsManagersGroupMember

# Create your views here.
# logger = logging.getLogger('debug')


class BoundTasks(ListAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'status', 'priority', 'create_date']
    ordering = ['id']

    # def get_queryset(self):
    #     assert self.queryset is not None, (
    #             "'%s' should either include a `queryset` attribute, "
    #             "or override the `get_queryset()` method."
    #             % self.__class__.__name__
    #     )
    #
    #     queryset = self.queryset
    #     if isinstance(queryset, QuerySet):
    #         # Ensure queryset is re-evaluated on each request.
    #         queryset = queryset.all()
    #     return queryset

    def get(self, request, *args, **kwargs):
        # print(request)
        # super().get(self, request, *args, **kwargs)
        if request.user.groups.filter(name='Managers').exists():
            queryset = Task.objects.filter(created_by=request.user.id)
        else:
            queryset = Task.objects.filter(executor=request.user.id)
        serializer = TaskSerializer(queryset, many=True)

        return Response(serializer.data)


class TaskListView(ListAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'status', 'priority', 'create_date']
    ordering = ['id']


class TaskCreateView(CreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = (IsManagersGroupMember, )

    def post(self, request):
        # logger.debug(request.data)
        task = request.data
        task['created_by'] = request.user.id
        serializer = TaskSerializer(data=task, context=request)
        print(request)

        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
            return Response({"success": "Task '{}' created successfully".format(task_saved.name)})
        else:
            return Response(serializer.errors)


class TaskUpdateView(RetrieveUpdateAPIView):

    serializer_class = TaskSerializer
    permission_classes = (IsManagersGroupMemberAndOwnerOrExecutor,)

    def put(self, request, pk):

        obj = Task.objects.get(id=pk)
        self.check_object_permissions(request, obj)

        data = request.data
        saved_task = get_object_or_404(Task.objects.all(), pk=pk)

        if request.user.groups.filter(name='Managers').exists():
            serializer = TaskManagerSerializer(instance=saved_task, data=data, context=request.user.id, partial=True)
        else:
            serializer = TaskDeveloperSerializer(instance=saved_task, data=data)

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
