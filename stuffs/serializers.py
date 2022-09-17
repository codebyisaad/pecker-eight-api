from copy import deepcopy

from django.db.models import Q
from rest_framework import serializers

from .models import Component, Group, Specification


class SpecificationSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.StringRelatedField(many=True, read_only=True)
    components = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Specification
        fields = "__all__"

    def validate_completed(self, value):
        if value and self.instance.components.filter(Q(part_code=None) | Q(part_code="")).exists():
            raise serializers.ValidationError("Cannot complete a specification if any component is missing a part.")

        return value

    def validate(self, data):
        if self.instance and self.instance.completed:
            raise serializers.ValidationError("Cannot modify a specification that has been completed.")

        return data


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    components = serializers.StringRelatedField(many=True, read_only=True)

    def __init__(self, *args, **kwargs):
        specification = kwargs.pop("specification", None)
        super().__init__(*args, **kwargs)

        self.specification = self.instance_specification or specification

    @property
    def instance_specification(self):
        if hasattr(self, "instance") and isinstance(self.instance, Component):
            return self.instance.specification
        return None

    def validate_group(self, value):
        if self.specification and value.specification != self.specification:
            raise serializers.ValidationError("Group must be in the same specification as the component.")

        return value


