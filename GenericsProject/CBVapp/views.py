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