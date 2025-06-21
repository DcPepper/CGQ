from rest_framework import serializers

from quiz.models import Geophraphy

class GeographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Geophraphy
        fields = '__all__'