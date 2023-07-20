from django.urls import include, path
from rest_framework_nested import routers

from stuffs import viewsets

router = routers.DefaultRouter()

router.register("specifications", viewsets.SpecificationViewSet, basename="specification")
router.register("groups", viewsets.GroupViewSet, basename="group")
router.register("components", viewsets.ComponentViewSet, basename="component")

