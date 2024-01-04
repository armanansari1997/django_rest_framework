from django.contrib import admin
from django.urls import path, include
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from CBVapp.views import CourseListView

router = DefaultRouter()
router.register('courses', CourseListView, basename='course')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
]
