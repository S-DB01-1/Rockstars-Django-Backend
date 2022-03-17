from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import Tribes, Rockstars, Articles
from .serializers import TribesSerializer, RockstarsSerializer, ArticlesSerializer


# Create your views here.
class TribesViewSet(
    RetrieveModelMixin,
    ListModelMixin
    ):

    serializer_class = TribesSerializer
    queryset = Tribes.objects.all()

class RockstarsViewSet(
    RetrieveModelMixin,
    ListModelMixin
    ):

    serializer_class = RockstarsSerializer
    queryset = Rockstars.objects.all()

class ArticlesViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin
    ):

    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()
