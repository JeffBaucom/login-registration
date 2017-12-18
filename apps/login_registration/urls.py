from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^users/create$', views.create),
    url(r'^users/login$', views.login)
]
