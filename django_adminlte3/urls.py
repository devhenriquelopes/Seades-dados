"""django_adminlte3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from adminlte3 import views
from adminlte3.views import graph_view

urlpatterns = [
    path('municipio/', views.IndexView.as_view(), name='municipio'),
    path('sisa/', views.EntregaSISAView.as_view(), name='sisa'),
    path('sisag/', views.EntregaSISAView.as_view(), name='sisa'),    
    path('sisa_alimentos/', views.AlimentosPeriodoListView.as_view(), name='alimentos_periodo'),
    url(r'^$', TemplateView.as_view(template_name='adminlte/index.html')),
    url(r'^login/$', TemplateView.as_view(template_name='adminlte/login.html')),
    path('admin/', admin.site.urls),
]
