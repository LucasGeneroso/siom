from rest_framework import serializers

from apps.occurrence.models import Occurrence


class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = [
            'id', 
            'type', 
            'city', 
            'state', 
            'neighborhood', 
            'street', 
            'complement', 
            'number', 
            'description', 
            'date', 
            'reported_by', 
            'image'
        ]
