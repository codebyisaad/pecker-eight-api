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


