from projects import models as m 
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Cart
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Task
        fields = '__all__'
