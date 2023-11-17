from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from . import serializers as s 
from . import models as m 


class ProjectRetrieveAPIView(APIView):
    def get(self, request):
        projects = m.Project.objects.all()
        serialized = s.ProjectSerializer(projects, many=True)
        return Response(status=200, data=serialized.data)


class ProjectCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serialized = s.ProjectSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        return Response(status=200, data=serialized.data)


class ProjectUpdateDeleteAPIView(APIView):
    def put(self, request, pk):
        instance = get_object_or_404(m.Project, pk=pk)
        if instance:
            serialized = s.ProjectSerializer(data=instance)
            serialized.is_valid(raise_exception=True)
            serialized.save()
            return Response(status=200, data=serialized.data)
        return Response(status=400)

    def patch(self, request, pk):
        instance = get_object_or_404(m.Project, pk=pk)
        serialized = s.ProjectSerializer(data=instance, partial=True)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(status=200, data=serialized.data)
    
    def delete(self, request, pk):
        instance = get_object_or_404(m.Project, pk=pk)
        if instance:
            instance.delete()
            return Response(status=200, data={"Message": "Deleted successfully"})
        