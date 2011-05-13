# -*- coding: utf-8 -*-
from django.db import models
from positions.fields import PositionField


class Request(models.Model):

    request_body = models.TextField()
    position = PositionField()

    class Meta:
        ordering = ('-id', 'position',)
