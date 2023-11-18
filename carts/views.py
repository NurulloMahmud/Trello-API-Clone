from projects import models as m 
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers as s
from django.shortcuts import get_object_or_404



class CartsListAPIView(APIView):
    def get(self, request, project_id):
        project = get_object_or_404(m.Project, pk=project_id)
        carts = m.Cart.objects.filter(project=project)
        if carts:
            serialized = s.CartSerializer(carts, many=True)
            return Response(status=200, data=serialized.data)
        return Response(status=400)


class CartUpdateDeleteAPIView(APIView):
    def put(self, request, pk):
        instance = get_object_or_404(m.Cart, pk=pk)
        serialized = s.CartSerializer(instance, data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status=200, data=serialized.data)
        return Response(status=400)
    
    def patch(self, request, pk):
        instance = get_object_or_404(m.Cart, pk=pk)
        serialized = s.CartSerializer(instance, data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status=200, data=serialized.data)
        return Response(status=400)
    
    def delete(self, request, pk):
        instance = get_object_or_404(m.Cart, pk=pk)
        serialized = s.CartSerializer(instance, data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(status=200, data=serialized.data)
        return Response(status=400)
