from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import Tribes, Rockstars, Articles
from .serializers import TribesSerializer, RockstarsSerializer, ArticlesSerializer
from rest_framework.viewsets import GenericViewSet

# Create your views here.
class TribesViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
    ):

    serializer_class = TribesSerializer
    queryset = Tribes.objects.all()

class RockstarsViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
    ):

    serializer_class = RockstarsSerializer
    queryset = Rockstars.objects.all()

class ArticlesViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
    ):

    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()
