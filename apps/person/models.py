# -*- coding: utf-8 -*-
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    day_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    jabber = models.CharField(max_length=100, blank=True, null=True)
    skype = models.CharField(max_length=100, blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s %s'%(self.name, self.last_name)
