from rest_framework import serializers
from tracking.models import PlayHub


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayHub
        fields = '__all__'
