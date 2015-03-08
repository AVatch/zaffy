from django.conf.urls import patterns, include, url
from django.contrib import admin


from rest_framework.authtoken import views as rest_views

from zaffy_api import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/$', views.api_root),

    url(r'^', include('zaffy.urls')),
    url(r'^', include('gen.urls')),
)

urlpatterns += [
    url(r'^api/v1/api-token-auth/', rest_views.obtain_auth_token)
]

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api/v1/api-auth/', include('rest_framework.urls',
                                      namespace='rest_framework')),
]
