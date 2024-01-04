from django.urls import path

from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]
