from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Component, Group, Specification


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

