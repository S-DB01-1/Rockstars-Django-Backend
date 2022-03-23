from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Tribes, Rockstars, Articles, OnDemandRequests


class OnDemandRequestsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = OnDemandRequests
        fields = '__all__'


class TribesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tribes
        fields = '__all__'


class RockstarsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Rockstars
        fields = '__all__'


class ArticlesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
