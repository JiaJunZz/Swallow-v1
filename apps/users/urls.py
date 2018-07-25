from django.conf.urls import url
from users.views import login
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^login/$',login,name="login"),

]