from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    lat  = serializers.FloatField()
    lng  = serializers.FloatField()
