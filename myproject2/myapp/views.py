from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# from django.views.decorators.csrf import csrf_exempt

# from rest_framework.parsers import JSONParser

from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def employee_list_view(request):
  if request.method == 'GET':
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail_view(request, pk):
  try:
    employee = Employee.objects.get(pk=pk)
  except Employee.DoesNotExist:
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)
  
  elif  request.method == 'PUT':
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_list_view(request):
  if request.method == 'GET':
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)