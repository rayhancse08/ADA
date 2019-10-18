from django.shortcuts import render
from rest_framework import viewsets
from tracking.models import Tracking
from tracking.serializer import TrackingSerializer


# Create your views here.

class TrackingViewSet(viewsets.ModelViewSet):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer
