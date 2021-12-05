from rest_framework import serializers


class CreateClientSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=80, required=True, trim_whitespace=True, min_length=3
    )
    prenom = serializers.CharField(
        max_length=80, required=True, trim_whitespace=True, min_length=3
    )
