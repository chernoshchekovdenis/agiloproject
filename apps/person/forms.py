# -*- coding: utf-8 -*-
from django import forms

from models import Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person