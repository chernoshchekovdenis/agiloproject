# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.template.response import TemplateResponse

from db_requests.models import Request


class RequestList(ListView):
    '''List of Requests'''
    
    model = Request
    context_object_name='request_list'
    template_name = 'db_requests/request-list.html'
    queryset = Request.objects.all()[:10]

    def post(self, request, id):
        obj_to_save = Request.objects.get(id=id)
        obj_to_save.position = request.POST['position']
        obj_to_save.save()
        request_list = Request.objects.all().order_by('-id','position')[:10]
        data = {
            'request_list': request_list,
        }
        return TemplateResponse(request, self.template_name, data)
