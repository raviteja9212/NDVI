from rest_framework import serializers
from .models import NDVIModel

class NDVISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NDVIModel
        fields = ['id', 'url', 'title', 'image']