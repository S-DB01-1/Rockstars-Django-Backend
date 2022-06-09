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
    Podcast_id = serializers.IntegerField(source='Podcast.id', read_only=True)

    class Meta:
        model = PodcastEpisodes
        fields = '__all__'

class PodcastSerializer(HyperlinkedModelSerializer):
    episodes = PodcastEpisodeSerializer(many=True)
    id = serializers.IntegerField(source='podcastid', read_only=True)
    tribeid = serializers.IntegerField(source='tribe.tribeid', read_only=True)
    rockstarid = serializers.IntegerField(source='rockstar.rockstarid', read_only=True)

    class Meta:
        model = Podcast
        fields = ('__all__', 'episodes')



class VideoSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='videoid', read_only=True)
    tribeid = serializers.IntegerField(source='tribe.tribeid', read_only=True)

    class Meta:
        model = Video
        fields = (
            "videoid",
            "title",
            "description",
            "get_link",
            "date_created",
            "datemodified",
            "datepublished",
            "publishedstatus",
            "viewcount",
            "tribe",
            "rockstar",
        )


class ArticleTextSerializer(HyperlinkedModelSerializer):
    id = serializers.IntegerField(source='articletextblockid', read_only=True)

    class Meta:
        model = ArticleText
        fields = '__all__'
