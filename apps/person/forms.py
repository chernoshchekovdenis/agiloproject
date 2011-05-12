# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings

from models import Person


class CalendarWidget(forms.TextInput):
    class Media:
        js = (
            settings.STATIC_URL + 'js/jquery-ui-1.8.12/js/jquery-ui-1.8.12.custom.min.js',
        )
        css = {
            'all': (settings.STATIC_URL + 'js/jquery-ui-1.8.12/css/smoothness/jquery-ui-1.8.12.custom.css', ),
        }

    def __init__(self):
        super(CalendarWidget, self).__init__(attrs={'class': 'calendar_field'})


class PersonForm(forms.ModelForm):

    day_of_birth = forms.DateField(widget=CalendarWidget())

    class Meta:
        model = Person
        fields = ('other', 'skype', 'jabber', 'bio', 'day_of_birth', 'email', 'last_name', 'name')
