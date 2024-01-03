from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer


# Create your views here.
@csrf_exempt
def employee_list_view(request):
  if request.method == 'GET':
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)
  
  elif request.method == 'POST':
    json_data = JSONParser().parse(request)
    serializer = EmployeeSerializer(data=json_data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, safe=False, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def employee_detail_view(request, pk):
  try:
    employee = Employee.objects.get(pk=pk)
  except Employee.DoesNotExist:
    return HttpResponse(status=404)
  
  if request.method == 'GET':
    serializer = EmployeeSerializer(employee)
    return JsonResponse(serializer.data, safe=False)
  
  elif  request.method == 'PUT':
    json_data = JSONParser().parse(request)
    serializer = EmployeeSerializer(employee, data=json_data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, safe=False)
    return JsonResponse(serializer.errors, status=400)
  
  elif request.method == 'DELETE':
    employee.delete()
    return HttpResponse(status=204)


def user_list_view(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return JsonResponse(serializer.data, safe=False)