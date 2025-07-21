from django.shortcuts import render
from .serializers import ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProjectOwner

# Create your views here.
class ProjectView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProjectDetailView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        self.check_object_permissions(request, project)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        self.check_object_permissions(request, project)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)