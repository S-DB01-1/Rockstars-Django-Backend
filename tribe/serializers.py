from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Tribes, Rockstars, Articles, OnDemandRequests, Podcasts, Videos


class OnDemandRequestsSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = OnDemandRequests
        fields = '__all__'


class TribesSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Tribes
        fields = '__all__'


class RockstarsSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Rockstars
        fields = '__all__'


class ArticlesSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Articles
        fields = '__all__'


class PodcastsSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Podcasts
        fields = '__all__'


class VideosSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Videos
        fields = '__all__'