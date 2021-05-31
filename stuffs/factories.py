# stuffs/factories.py

import factory
from factory.django import DjangoModelFactory

class SpecificationFactory(DjangoModelFactory):
    class Meta:
        model = Specification

    name = factory.Faker("word")
    code_number = factory.Faker("ean8")
    completed = False
    status = "Planning Phase"


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Faker("word")
    group_code = factory.Faker("ean8")
    specification = factory.SubFactory(SpecificationFactory)


