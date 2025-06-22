from rest_framework import serializers

from quiz.models import Geophraphy

class GeographySerializer(serializers.HyperlinkedModelSerializer):
    get_main_fields = serializers.CharField()
    get_filter_fields = serializers.CharField()
    class Meta:
        model = Geophraphy
        fields = '__all__'
        read_only_fields = (
        'get_main_fields',
        )