from rest_framework import generics

from .models import Course
from .serializers import CourseSerializer

# Create your views here.

class CourseListView(generics.ListCreateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  
  
"""  
class CourseListView(generics.ListAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer  

class CourseListView(generics.CreateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer  
"""


"""
class CourseDetailView(generics.RetrieveAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  
class CourseDetailView(generics.UpdateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  
class CourseDetailView(generics.DestroyAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveDestroyAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
"""
  