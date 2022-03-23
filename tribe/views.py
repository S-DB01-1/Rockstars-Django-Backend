from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.core.mail import send_mail

from .models import Tribes, Rockstars, Articles
from .serializers import TribesSerializer, RockstarsSerializer, ArticlesSerializer


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
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()

    def retrieve(self, request, *args, **kwargs):
        # Fetch article by pk or return 404
        queryset = Articles.objects.filter(id=kwargs.get('pk'))
        article = get_object_or_404(queryset)

        # Update counter
        Articles.objects.filter(id=article.id).update(Viewcount=article.Viewcount + 1)

        serializer = ArticlesSerializer(article, context={'request': request})  # Passing context is required here
        return Response(serializer.data)
