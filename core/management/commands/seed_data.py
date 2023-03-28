from random import sample

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from stuffs.factories import ComponentFactory, GroupFactory, SpecificationFactory


