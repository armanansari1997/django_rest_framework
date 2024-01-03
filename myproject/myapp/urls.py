from django.urls import path
from .views import employee_list_view, user_list_view, employee_detail_view

urlpatterns = [
    path('api/employees', employee_list_view, name='employee_list'),
    path('api/employee/<int:pk>', employee_detail_view, name='employee_detail'),
    path('api/users', user_list_view, name='user_list'),
]
