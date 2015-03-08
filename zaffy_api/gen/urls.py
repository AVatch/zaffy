from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from gen import views

urlpatterns = patterns('',

    url(r'^api/v1/gen/zaffy/$', views.gen_zaffy),
)

urlpatterns += staticfiles_urlpatterns()
