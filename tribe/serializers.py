from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import ArticleText, Tribe, Rockstar, Article, OnDemandRequest, Podcast, Video, Tag, ArticleImage, PodcastEpisodes


class OnDemandRequestSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = OnDemandRequest
        fields = '__all__'


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TribeSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='tribeid', read_only=True)

    class Meta:
        model = Tribe
        fields = '__all__'


class RockstarSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='rockstarid', read_only=True)
    tribeid = serializers.IntegerField(source='tribe.tribeid', read_only=True)

    class Meta:
        model = Rockstar
        fields = '__all__'


class ArticleSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='articleid', read_only=True)
    tribeid = serializers.IntegerField(source='tribe.tribeid', read_only=True)
    author = serializers.CharField(source='rockstar.name', read_only=True)
    rockstarid = serializers.IntegerField(source='rockstar.rockstarid', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleImageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ArticleImage
        fields = '__all__'

class PodcastEpisodeSerializer(HyperlinkedModelSerializer):
    podcastid = serializers.IntegerField(source='podcast.id', read_only=True)

    class Meta:
        model = PodcastEpisodes
        fields = '__all__'

class PodcastSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='podcastid', read_only=True)
    tribeid = serializers.IntegerField(source='tribe.tribeid', read_only=True)
    episodes = PodcastEpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'tribeid', 'episodes'])



class VideoSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='videoid', read_only=True)
    tribeid = serializers.IntegerField(source='tribe.tribeid', read_only=True)
    getlink = serializers.CharField(source='get_link', read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


class ArticleTextSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='articletextblockid', read_only=True)

    class Meta:
        model = ArticleText
        fields = '__all__'
