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


    def test_validate_modification_of_completed_specification(self):
        self.specification.completed = True
        self.specification.save()
        serializer = SpecificationSerializer(self.specification, data={"name": "New Name"}, partial=True)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

class GroupSerializerTest(TestCase):
    def setUp(self):
        self.specification = SpecificationFactory()
        self.group = GroupFactory(specification=self.specification)

    def test_validate_name(self):
        another_specification = SpecificationFactory()
        GroupFactory(name="Test Group", specification=another_specification)
        serializer = GroupSerializer(
            data={"name": "Test Group", "group_code": "GRP004"}, specification=self.specification
        )
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

