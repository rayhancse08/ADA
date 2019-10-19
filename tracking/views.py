from django.shortcuts import render
from rest_framework import viewsets
from tracking.models import PlayHub
from tracking.serializer import TrackingSerializer


# Create your views here.

class TrackingViewSet(viewsets.ModelViewSet):
    queryset = PlayHub.objects.all()
    serializer_class = TrackingSerializer
