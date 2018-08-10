from django.conf.urls import url
from users.views import login


urlpatterns = [
    url(r'^login/$',login,name="login"),

]