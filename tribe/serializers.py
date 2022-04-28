from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Tribes, Rockstars, Articles, OnDemandRequests, Podcasts, Videos, PodcastEpisodes


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
    Tribe_id = serializers.IntegerField(source='Tribe.id', read_only=True)

    class Meta:
        model = Rockstars
        fields = '__all__'


class ArticlesSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    Tribe_id = serializers.IntegerField(source='Tribe.id', read_only=True)
    Author = serializers.CharField(source='Rockstar.Name', read_only=True)

    class Meta:
        model = Articles
        fields = '__all__'


class PodcastsSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    Tribe_id = serializers.IntegerField(source='Tribe.id', read_only=True)
    Rockstar_id = serializers.IntegerField(source='Rockstar.id', read_only=True)

    class Meta:
        model = Podcasts
        fields = '__all__'


class PodcastEpisodesSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    Podcast_id = serializers.IntegerField(source='Podcast.id', read_only=True)

    class Meta:
        model = PodcastEpisodes
        fields = '__all__'


class VideosSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    Tribe_id = serializers.IntegerField(source='Tribe.id', read_only=True)

    class Meta:
        model = Videos
        fields = '__all__'
