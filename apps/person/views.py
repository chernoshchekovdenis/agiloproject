# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import View
from django.template.response import TemplateResponse
from django.contrib.auth import logout

from django.contrib.auth.models import User
from models import Person
from forms import PersonForm


class PersonEdit(View):

    model = Person
    template_name = 'person/update-form.html'
    instance = Person.objects.get(id=1)

    def get(self, request):
        form = PersonForm(instance=self.instance)
        return TemplateResponse(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = PersonForm(request.POST, request.FILES, instance=self.instance)
        if form.is_valid():
            object_to_save = form.save(commit=False)
            object_to_save.save()
            logout(request)
            return HttpResponseRedirect(reverse('home-page'))
        else:
            form = PersonForm(request.POST, request.FILES, instance=self.instance)
            data = {
                    'form':form,
                    }
            return TemplateResponse(request, self.template_name, data)
