from django.db import models
from django.urls import reverse
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import StatusModel, TimeStampedModel

    name = models.CharField(max_length=200)
    code_number = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    status = StatusField(choices=STATUS)

    objects = models.Manager()
    reports = SpecificationReportManager()

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name

