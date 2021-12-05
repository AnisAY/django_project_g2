from rest_framework import serializers
from clients import models


class ClientReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = serializers.ALL_FIELDS
