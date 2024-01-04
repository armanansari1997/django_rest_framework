from rest_framework import mixins, generics

from .models import Course
from .serializers import CourseSerializer

# Create your views here.

class CourseListView(mixins.ListModelMixin, 
                     mixins.CreateModelMixin, 
                     generics.GenericAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  
  def get(self, request):
    return self.list(request)
  
  def post(self, request):
    return self.create(request)
  
  
class CourseDetailView(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  
  def get(self, request, pk):
    return self.retrieve(request, pk)
  
  def put(self, request, pk):
    return self.update(request, pk)

  def delete(self, request, pk):
    return self.destroy(request, pk)  
  