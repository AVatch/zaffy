from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from zaffy import views


# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/v1/zaffy/$',
        views.ZaffyList.as_view(),
        name='zaffy-list'),

    url(r'^api/v1/zaffy/(?P<pk>[0-9]+)/$',
        views.ZaffyDetails.as_view(),
        name='zaffy-detail'),
])
