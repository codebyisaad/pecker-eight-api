import pandas as pd
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.viewmixins import NestedObjectMixin
from core.viewsets import CreateListViewSet, RetrieveUpdateDestroyViewset

from .models import Component, Group, Specification
from .serializers import (
    ComponentSerializer,
    GroupSerializer,
    PartCodeAssignmentSerializer,
    SpecificationCloneSerializer,
    SpecificationImportSerializer,
    SpecificationSerializer,
)


class SpecificationViewSet(ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer

    @action(detail=True, methods=["post"], serializer_class=SpecificationCloneSerializer)
    def clone(self, request, *args, **kwargs):
        specification = self.get_object()
        serializer = self.get_serializer(data=request.data, specification=specification)

        if serializer.is_valid():
            cloned_specification = serializer.clone()
            specification_serializer = SpecificationSerializer(cloned_specification, context={"request": request})

            return Response(
                {"status": "Specification cloned successfully!", "cloned": specification_serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], serializer_class=SpecificationImportSerializer)
    def import_data(self, request):
        serializer = SpecificationImportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "Specifications imported successfully!"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def export_built_specification_report(self, request):
        built_count = Specification.reports.built_count()
        df = pd.DataFrame.from_records(built_count)

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="built_specifications_report.csv"'

        df.to_csv(path_or_buf=response, index=False, header=["Specification Code", "Number of Built Specifications"])

        return response


class BaseNestedSpecificationViewSet(NestedObjectMixin, CreateListViewSet):
    parent_model = Specification
    parent_object_lookup_field = "specification_pk"

    def get_serializer(self, *args, **kwargs):
        kwargs.update(specification=self.get_parent_object())

        return super().get_serializer(*args, **kwargs)

