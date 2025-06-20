from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Component, Group, Specification


class ImportSpecificationsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/stuffs/specifications/import_data/"
        self.valid_payload = {
            "specifications": [
                {
                    "name": "Specification 1",
                    "code_number": "SPEC001",
                    "completed": False,
                    "status": "Planning Phase",
                    "groups": [
                        {
                            "name": "Group 1",
                            "group_code": "GRP001",
                            "components": [
                                {"name": "Component 1", "description": "This is component 1", "part_code": "PART001"},
                                {"name": "Component 2", "description": "This is component 2", "part_code": "PART002"},
                            ],
                        },
                        {
                            "name": "Group 2",
                            "group_code": "GRP002",
                            "components": [
                                {"name": "Component 3", "description": "This is component 3", "part_code": "PART003"}
                            ],
                        },
                    ],
                }
            ]
        }

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Specification.objects.count(), 1)
        self.assertEqual(Group.objects.count(), 2)
        self.assertEqual(Component.objects.count(), 3)

