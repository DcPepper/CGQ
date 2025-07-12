from rest_framework import serializers

from quiz.models import Geophraphy, Japanese

class GeographySerializer(serializers.HyperlinkedModelSerializer):
    get_main_fields = serializers.CharField()
    get_filter_fields = serializers.CharField()
    class Meta:
        model = Geophraphy
        fields = '__all__'
        read_only_fields = (
        'get_main_fields',
        )

class JapaneseSerializer(serializers.HyperlinkedModelSerializer):
    get_main_fields = serializers.CharField()
    get_filter_fields = serializers.CharField()
    class Meta:
        model = Japanese
        fields = '__all__'
        read_only_fields = (
        'get_main_fields',
        )