# -*- coding: utf-8 -*-
from django.views.generic import ListView
from db_requests.models import Request


class RequestList(ListView):
    '''List of Requests'''
    
    model = Request
    context_object_name='request_list'
    template_name = 'db_requests/request-list.html'

    def get_queryset(self):
        return Request.objects.all()[:10]
