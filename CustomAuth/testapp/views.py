from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from rest_framework.permissions import IsAuthenticated
from .authentication import CustomAuthentication
from .authentication_two import CustomAuthentictionTwo
from .serializer import EmployeeSerializer
# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [CustomAuthentication,]
    permission_classes = [IsAuthenticated,]

class EmployeeCRUDCBV2(ModelViewSet):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
        authentication_classes = [CustomAuthentictionTwo]
        permission_classes = [IsAuthenticated, ]
