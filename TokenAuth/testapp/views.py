from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Employee
from.serializers import EmloyeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from testapp.permission import SunnyPremission,IsReadOnly
# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmloyeeSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsReadOnly,]