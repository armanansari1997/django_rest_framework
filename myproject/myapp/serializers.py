from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=50)
  email = serializers.EmailField()
  password = serializers.CharField(max_length=50)
  phone = serializers.CharField(max_length=10)
  
  def create(self, validated_data):
    """
    Create and return a new `Employee` instance, given the validated data.
    """
    return Employee.objects.create(**validated_data)
  
  def update(self, employee, validated_data):
    """
      Update and return an existing `Snippet` instance, given the validated data.
    """
    new_emp = Employee(**validated_data)
    new_emp.id = employee.id
    new_emp.save()
    return new_emp


class UserSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=50)
  email = serializers.EmailField()
  password = serializers.CharField(max_length=50)
  first_name = serializers.CharField(max_length=50)
  last_name = serializers.CharField(max_length=50)