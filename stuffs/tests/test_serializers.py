from django.test import TestCase
from rest_framework.exceptions import ValidationError

from stuffs.factories import ComponentFactory, GroupFactory, SpecificationFactory
from stuffs.serializers import (
    ComponentSerializer,
    GroupSerializer,
    PartCodeAssignmentSerializer,
    SpecificationCloneSerializer,
    SpecificationSerializer,
)

