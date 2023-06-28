"""
URL configuration for CrudProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls.conf import include
from .views import index
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('add_item/',add_item,name='add_item'),
    path('delete_item/<int:myid>/',delete_item,name='delete_item'),
    path('edit_item/<int:myid>/',edit_item,name='edit_item'),
    path('update_item/<int:myid>/',update_item,name='update_item'),
]
