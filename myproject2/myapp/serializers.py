from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'
    # fields = ('name', 'email')


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    # fields = ['username', 'password', 'email']
    # fields = '__all__'
    exclude = ['email', 'password']