from django.shortcuts import render
from rest_framework import viewsets
from tracking.models import PlayHub
from tracking.serializer import TrackingSerializer
from rest_framework import viewsets, mixins


# Create your views here.

class TrackingViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
                      mixins.ListModelMixin):
    queryset = PlayHub.objects.all()
    serializer_class = TrackingSerializer
