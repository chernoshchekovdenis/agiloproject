# -*- coding: utf-8 -*-
from tddspry.django import TestCase

from db_requests.models import Request


class RequestListTest(TestCase):
    
    def setup(self):
        self.request = Request(request_body='')

    def test_request_list(self):
        self.go200(self.build_url('request-list'))