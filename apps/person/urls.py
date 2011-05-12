# -*- encoding: utf-8 -*-
from django.conf.urls.defaults import *
from apps.person.views import *


urlpatterns = patterns('',
    url(r'^$', PersonEdit.as_view(), name="person-edit"),
)