from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Tribe, Rockstar, Article, OnDemandRequest, Podcast, Video
from .serializers import TribeSerializer, RockstarSerializer, ArticleSerializer, OnDemandRequestSerializer, \
    PodcastSerializer, VideoSerializer


# This function works for the retrieve functions that currently use it, but because the other teams database table pk
# isn't called 'id' this currently won't work for example on the podcast episode table. I'm currently not going to
# invest time in fixing this since we'll probably get rid of this entire function in the near future
def retrieve_update_counter(request, model, serializer, *args, **kwargs):
    queryset = model.objects.filter(articleid=kwargs.get('pk'))
    instance = get_object_or_404(queryset)

    # Update counter
    model.objects.filter(articleid=instance.articleid).update(viewcount=instance.viewcount + 1)

    serializer = serializer(instance, context={'request': request})  # Passing context is required here
    return Response(serializer.data)


class TribeViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = TribeSerializer
    queryset = Tribe.objects.all()


class RockstarViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = RockstarSerializer
    queryset = Rockstar.objects.all()

    def get_queryset(self):
        queryset = Rockstar.objects.all()
        tribe = self.request.query_params.get('tribe')
        if tribe is not None:
            queryset = queryset.filter(tribe_id=tribe)
        return queryset


class ArticleViewSet(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = Article.objects.all()
        tribe = self.request.query_params.get('tribe')
        if tribe is not None:
            queryset = queryset.filter(tribe_id=tribe)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        return retrieve_update_counter(request, Article, ArticleSerializer, *args, **kwargs)


class OnDemandRequestViewSet(
    GenericViewSet
):
    serializer_class = OnDemandRequestSerializer
    queryset = OnDemandRequest.objects.all()

    def create(self, request):
        # Fetch data from POST
        name = request.data['name']
        company = request.data['company']
        email = request.data['email']
        phone_number = request.data['phone_number']
        date = request.data['date']
        subject = request.data['subject']

        # Create entry in db
        OnDemandRequest.objects.create(Name=name, PhoneNumber=phone_number, Date=date, Subject=subject)

        # Render template
        context = {'name': name, 'company': company, 'date': date, 'subject': subject}
        html_message = render_to_string('mail_template/RockstarEmailConfirmation.html', context)
        plain_message = strip_tags(html_message)

        to = ['rockstarsdjangobackend@gmail.com', email]
        subject = 'Requested Speaker'
        send_mail(subject=subject, message=plain_message, html_message=html_message, recipient_list=to,
                  from_email=None)  # Use default from e-mail and allow plain text message where HTML is unsupported

        return Response(status=status.HTTP_201_CREATED)


class PodcastViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = PodcastSerializer
    queryset = Podcast.objects.all()

    def get_queryset(self):
        queryset = Podcast.objects.all()
        tribe = self.request.query_params.get('tribe')
        if tribe is not None:
            queryset = queryset.filter(tribe_id=tribe)

        rockstar = self.request.query_params.get('rockstar')
        if rockstar is not None:
            queryset = queryset.filter(rockstar_id=rockstar)

        return queryset


# Currently disabled till the other group fixes their tables.
# class PodcastEpisodeViewSet(
#     RetrieveModelMixin,
#     ListModelMixin,
#     GenericViewSet
# ):
#     serializer_class = PodcastEpisodeSerializer
#     queryset = PodcastEpisodes.objects.all()
#
#     def get_queryset(self):
#         queryset = PodcastEpisodes.objects.all()
#         podcast = self.request.query_params.get('podcast')
#         if podcast is not None:
#             queryset = queryset.filter(Podcast_id=podcast)
#
#         return queryset


class VideoViewset(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return retrieve_update_counter(request, Video, VideoSerializer, *args, **kwargs)

    def get_queryset(self):
        queryset = Video.objects.all()
        tribe = self.request.query_params.get('tribe')
        if tribe is not None:
            queryset = queryset.filter(tribe_id=tribe)
        return queryset
