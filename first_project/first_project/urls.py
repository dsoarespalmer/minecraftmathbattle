"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add.html', views.add, name='add'),
    path('subtract.html', views.subtract, name='subtract'),
    path('multiply.html', views.multiply, name='multiply'),
    path('divide.html', views.divide, name='divide'),
    path('admin/', admin.site.urls),
    path('formpage/',views.form_name_view,name='form_name'),
]
