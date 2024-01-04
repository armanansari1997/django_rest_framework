from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import Course
from .serializers import CourseSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class CourseListView(ViewSet):
  def list(self, request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    queryset = Course.objects.all()
    course = get_object_or_404(queryset, pk=pk)
    serializer = CourseSerializer(course)
    return Response(serializer.data)
  
  def create(self, request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def update(self, request, pk):
    course = get_object_or_404(course, pk=pk)
    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def destroy(self, request, pk):
    course = get_object_or_404(course, pk=pk)
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
