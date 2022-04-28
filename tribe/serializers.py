from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Tribe, Rockstar, Article, OnDemandRequest, Podcast, Video, Tag, ArticleImage


class OnDemandRequestSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = OnDemandRequest
        fields = '__all__'


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TribeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tribe
        fields = '__all__'


class RockstarSerializer(HyperlinkedModelSerializer):
    tribe_id = serializers.IntegerField(source='tribe.tribeid', read_only=True)

    class Meta:
        model = Rockstar
        fields = '__all__'


class ArticleSerializer(HyperlinkedModelSerializer):
    tribeid = serializers.IntegerField(source='tribe.tribeid', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleImageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ArticleImage
        fields = '__all__'


class PodcastSerializer(HyperlinkedModelSerializer):
    tribeid = serializers.IntegerField(source='tribe.tribeid', read_only=True)
    rockstarid = serializers.IntegerField(source='rockstar.rockstarid', read_only=True)

    class Meta:
        model = Podcast
        fields = '__all__'


# class PodcastEpisodeSerializer(HyperlinkedModelSerializer):
#     
#     Podcast_id = serializers.IntegerField(source='Podcast.id', read_only=True)
#
#     class Meta:
#         model = PodcastEpisodes
#         fields = '__all__'


class VideoSerializer(HyperlinkedModelSerializer):
    tribeid = serializers.IntegerField(source='tribe.tribeid', read_only=True)

    class Meta:
        model = Video
        fields = '__all__'
