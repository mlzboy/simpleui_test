"""simpleui_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from login.views import index
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.views.generic.base import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simditor/', include('simditor.urls')),
    path('questions/', include('oj.urls')),
    path('login/', include('login.urls')),
    # path('captcha/', include('captcha.urls')),
    path('', index),
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
