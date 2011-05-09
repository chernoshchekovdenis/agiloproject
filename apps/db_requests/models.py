# -*- coding: utf-8 -*-
from django.db import models


class Request(models.Model):

    request_body = models.TextField()

    class Meta:
        ordering = ('-id',)
