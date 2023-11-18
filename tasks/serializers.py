from rest_framework.serializers import ModelSerializer
from projects import models as m 


class TaskSerializer(ModelSerializer):
    class Meta:
        model = m.Task
        fields = '__all__'
