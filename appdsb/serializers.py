# serializers.py
from rest_framework import serializers
from .models import DSB


class DSBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DSB
        fields = ('id', 'temp', 'dt')
