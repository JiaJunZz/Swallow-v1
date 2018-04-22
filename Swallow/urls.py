"""Swallow URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from asset import views as asset_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',TemplateView.as_view(template_name="index.html"),name="index"),
    url(r'^asset_server/$',asset_views.asset_server,name="asset_server"),
    url(r'^server_add/$',asset_views.server_add,name="server_add"),
    url(r'^server_del/$',asset_views.server_del,name="server_del"),
]