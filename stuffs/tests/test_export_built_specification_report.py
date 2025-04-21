from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ..factories import SpecificationFactory


class BuiltSpecificationsReportTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/stuffs/specifications/export_built_specification_report/"

