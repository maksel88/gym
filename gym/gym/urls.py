"""gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from person import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    # re_path(r'^about/contact', views.contact),
    re_path(r'^home', views.home),
    # re_path(r'^products/$', views.products),
    # re_path(r'^products/(?P<productid>\d+)/', views.products),
    # re_path(r'^users/$', views.users),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    # path('products/<int:productid>/', views.products),
    # path('users/', views.users),
]
