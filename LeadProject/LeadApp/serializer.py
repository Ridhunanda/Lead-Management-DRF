from rest_framework import serializers
from LeadApp.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    # source=serializers.ChoiceField(choices=Lead.SOURCE_CHOICES)   # if we are using serializer instead of modelserializer
    class Meta:
        model=Lead
        fields="__all__"
        read_only_fields=['id','added_date']

    