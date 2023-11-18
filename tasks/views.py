from rest_framework.views import APIView
from rest_framework.response import Response
from projects import models as m 
from .serializers import TaskSerializer
from django.shortcuts import get_list_or_404


class TasksListAPIView(APIView):
    def get(self, request, cart_id):
        tasks = get_list_or_404(m.Task, id=cart_id)
        serialized = TaskSerializer(tasks, many=True)
        if serialized:
            return Response(status=200, data=serialized.data)
        return Response(status=400)