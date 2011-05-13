from django.conf.urls.defaults import patterns, url
from db_requests.views import *


urlpatterns = patterns('',
    url(r'^$', RequestList.as_view(), name='request-list'),
    url(r'^edit/(?P<id>.*)/$', RequestList.as_view(), name='request-edit'),
)
