"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from intro_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('bears', views.one_method),                        # would only match localhost:8000/bears
    path('bears/<my_val>', views.another_method),    # would match localhost:8000/bears/23
    path('bears/<name>', views.yet_another),    # would match localhost:8000/bears/pooh/poke
    path('<id>/<color>', views.one_more),  # would match localhost:8000/17/brown
]
