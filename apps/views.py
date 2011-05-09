# -*- coding: utf-8 -*-
from django.views.generic import View
from django.template.response import TemplateResponse

from person.models import Person
from db_requests.models import Request


class HomePage(View):

    template_name = 'home.html'

    def get(self, request):
        person, created = Person.objects.get_or_create(name='Denis', last_name='Chernoshchekov')
        requests = Request.objects.all()

        data = {
            "person": person,
            "requests": requests,
        }
        return TemplateResponse(request, self.template_name, data)
