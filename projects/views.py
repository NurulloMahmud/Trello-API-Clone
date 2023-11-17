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
        if serialized.is_valid():
            serialized.save()
            return Response(status=200, data=serialized.data)
        return Response(serialized.errors, status=400)


class ProjectUpdateDeleteAPIView(APIView):
    def put(self, request, pk):
        instance = get_object_or_404(m.Project, pk=pk)
        serialized = s.ProjectSerializer(instance, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(status=200, data=serialized.data)
        return Response(serialized.errors, status=400)

    def patch(self, request, pk):
        instance = get_object_or_404(m.Project, pk=pk)
        serialized = s.ProjectSerializer(instance, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=200, data=serialized.data)
        return Response(serialized.errors, status=400)
    
    def delete(self, request, pk):
        instance = get_object_or_404(m.Project, pk=pk)
        instance.delete()
        return Response(status=200, data={"Message": "Deleted successfully"})
    