# -*- coding: utf-8 -*-
from db_requests.models import Request


class RequestToDbMiddleware(object):
    
    def process_request(self, request):
        obj_to_save = Request(request_body=repr(request.__dict__))
        obj_to_save.save()
