from rest_framework import serializers
from todofeature.models import Task

# class TaskSerializer(serializers.Serializer):
    # title = serializers.CharField()
    
    
class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = ("name","description","image","task_date","priority","category","is_done",)    