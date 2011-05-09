# -*- coding: utf-8 -*-
from tddspry.django import TestCase

from person.models import Person


class PersonTest(TestCase):
    def setup(self):
        self.person = Person.objects.get(id=1)

    def test_home_page(self):
        self.find(self.person.name)
        self.find(self.person.last_name)
        self.find(self.person.day_of_birth.strftime('%B %d, %Y'))
        self.find(self.person.bio)
        self.find(self.person.email)
        self.find(self.person.jabber)
        self.find(self.person.skype)
        self.find(self.person.other)
