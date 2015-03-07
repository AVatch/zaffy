from django.conf.urls import patterns, url

from gen import views

urlpatterns = patterns('',

    url(r'^api/v1/gen/zaffy/$', views.gen_zaffy),
)
