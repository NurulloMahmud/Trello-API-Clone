from rest_framework import serializers
from . import models as m 


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Project
        fields = '__all__'


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.ProjectMember
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Cart
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Task
        fields = '__all__'
