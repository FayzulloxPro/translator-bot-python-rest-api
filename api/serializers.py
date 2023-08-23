from rest_framework import serializers
from .models import TranslationResponse


class TranslationResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationResponse
        fields = ('__all__')
