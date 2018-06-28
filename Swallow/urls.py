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
    url(r'^search/$',asset_views.server_search,name="server_search"),
    url(r'^output_excel/$',asset_views.output_excel,name="output_excel"),
    url(r'^server_add/$',asset_views.server_add,name="server_add"),
    url(r'^server_del/$',asset_views.server_del,name="server_del"),
    url(r'^server_edit/(\d+)/$',asset_views.server_edit,name="server_edit"),
    url(r'^server_detail/(\d+)/$',asset_views.server_detail,name="server_detail"),
    url(r'supplier_add/$',asset_views.supplier_add,name="supplier_add"),
    url(r'supplier_edit/(\d+)/$',asset_views.supplier_edit,name="supplier_edit"),
    url(r'supplier_del/(\d+)/$', asset_views.supplier_del, name="supplier_del"),
    url(r'manufactory_add/$',asset_views.manufactory_add,name="manufactory_add"),
    url(r'manufactory_edit/(\d+)/$',asset_views.manufactory_edit,name="manufactory_edit"),
    url(r'manufactory_del/(\d+)/$', asset_views.manufactory_del, name="manufactory_del"),
    url(r'^change_filter/$',asset_views.change_filter,name='change_filter'),
    url(r'^home/$',asset_views.home,name='home')
]
