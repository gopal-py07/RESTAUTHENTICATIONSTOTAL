from django.shortcuts import render
from rest_framework .viewsets import ModelViewSet
from .serializer import EmployeeSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from  .models import Employee
# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
   # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
