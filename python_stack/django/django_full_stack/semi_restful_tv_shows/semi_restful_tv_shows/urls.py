"""semi_restful_tv_shows URL Configuration

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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('shows',views.all_shows),
    path('shows/new',views.new_show),
    path('shows/create',views.create_show),
    path('shows/<id>',views.show_details),
    path('shows/<id>/edit',views.edit_show),
    path('shows/<id>/update',views.update_show),
    path('shows/<id>/delete',views.delete_show),
]
