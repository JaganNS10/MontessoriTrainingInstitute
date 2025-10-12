"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='Home'),
    path('about/',views.About,name='about'),
    path('academics/',views.Academics,name='academics'),
    path('admissions/',views.Admissions,name='admissions'),
    path('campus-facilities/',views.Campus_facilities,name='campus-facilities'),
    path('contact/',views.Contact,name='contact'),
    path('faculty-staff/',views.Faculty_staff,name='faculty-staff'),
    path('Error/',views.Error,name='404')
]
