from django.conf.urls import url
from api_project.api_app import views

urlpatterns = [
    url(r'^api/v1/clusters/cluster1/hosts/wlx-1-node$', views.host_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.host_detail),
]