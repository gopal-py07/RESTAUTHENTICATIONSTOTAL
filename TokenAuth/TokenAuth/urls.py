"""TokenAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from testapp import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api',views.EmployeeCRUDCBV)
from rest_framework.authtoken import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include(router.urls)),
    url('get-api-token',views.obtain_auth_token,name='get-api-token')

]
