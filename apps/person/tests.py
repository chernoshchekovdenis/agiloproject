# -*- coding: utf-8 -*-
from tddspry.django import TestCase

from person.models import Person


class PersonTest(TestCase):
    def setup(self):
        self.person = Person.objects.get(id=1)

    def test_home_page(self):
        self.go200(self.build_url('home-page'))
        self.find(self.person.name)
        self.find(self.person.last_name)
        self.find(self.person.day_of_birth.strftime('%d.%m.%Y'))
        self.find(self.person.bio)
        self.find(self.person.email)
        self.find(self.person.jabber)
        self.find(self.person.skype)
        self.find(self.person.other)

class PersonEditTest(TestCase):
    def setup(self):
        self.person = Person.objects.get(id=1)

    def test_update_not_authorized(self):
        edit_url = self.build_url('person-edit', args=(1,))
        response = self.client.get(edit_url, follow=True)
        self.assertEqual(response.status_code, 404)

    def test_update_authorized(self):
        self.client.login(username='freeman', password='1')
        edit_url = self.build_url('person-edit')
        response = self.client.get(edit_url, follow=True)
        self.assertEqual(response.status_code, 200)
