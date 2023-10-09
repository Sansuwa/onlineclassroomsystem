from rest_framework import viewsets
from todofeature.models import Task
from todofeature.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer