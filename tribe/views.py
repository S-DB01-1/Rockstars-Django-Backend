from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Tribes, Rockstars, Articles, OnDemandRequests, Podcasts, Videos, PodcastEpisodes
from .serializers import TribesSerializer, RockstarsSerializer, ArticlesSerializer, OnDemandRequestsSerializer, \
    PodcastsSerializer, VideosSerializer, PodcastEpisodesSerializer


def retrieve_update_counter(request, model, serializer, *args, **kwargs):
    queryset = model.objects.filter(id=kwargs.get('pk'))
    instance = get_object_or_404(queryset)

    # Update counter
    model.objects.filter(id=instance.id).update(Viewcount=instance.Viewcount + 1)

    serializer = serializer(instance, context={'request': request})  # Passing context is required here
    return Response(serializer.data)


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

    def get_queryset(self):
        queryset = Rockstars.objects.all()
        tribe = self.request.query_params.get('tribe')
        if tribe is not None:
            queryset = queryset.filter(Tribe_id=tribe)
        return queryset


class ArticlesViewSet(
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()

    def get_queryset(self):
        queryset = Articles.objects.all()
        tribe = self.request.query_params.get('tribe')
        if tribe is not None:
            queryset = queryset.filter(Tribe_id=tribe)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        return retrieve_update_counter(request, Articles, ArticlesSerializer, *args, **kwargs)


class OnDemandRequestsViewSet(
    GenericViewSet
):
    serializer_class = OnDemandRequestsSerializer
    queryset = OnDemandRequests.objects.all()

    def create(self, request):
        # Fetch data from POST
        name = request.data['name']
        company = request.data['company']
        email = request.data['email']
        phone_number = request.data['phone_number']
        date = request.data['date']
        subject = request.data['subject']

        # Create entry in db
        OnDemandRequests.objects.create(Name=name, PhoneNumber=phone_number, Date=date, Subject=subject)

        # Render template
        context = {'name': name, 'company': company, 'date': date, 'subject': subject}
        html_message = render_to_string('mail_template/RockstarEmailConfirmation.html', context)
        plain_message = strip_tags(html_message)

        to = ['rockstarsdjangobackend@gmail.com', email]
        subject = 'Requested Speaker'
        send_mail(subject=subject, message=plain_message, html_message=html_message, recipient_list=to,
                  from_email=None)  # Use default from e-mail and allow plain text message where HTML is unsupported

        return Response(status=status.HTTP_201_CREATED)


class PodcastsViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = PodcastsSerializer
    queryset = Podcasts.objects.all()

    def get_queryset(self):
        queryset = Podcasts.objects.all()
        tribe = self.request.query_params.get('tribe')
        if tribe is not None:
            queryset = queryset.filter(Tribe_id=tribe)

        rockstar = self.request.query_params.get('rockstar')
        if rockstar is not None:
            queryset = queryset.filter(Rockstar_id=rockstar)

        return queryset


class PodcastEpisodeViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = PodcastEpisodesSerializer
    queryset = PodcastEpisodes.objects.all()

    def get_queryset(self):
        queryset = PodcastEpisodes.objects.all()
        podcast = self.request.query_params.get('podcast')
        if podcast is not None:
            queryset = queryset.filter(Podcast_id=podcast)

        return queryset


class VideosViewset(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = VideosSerializer
    queryset = Videos.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return retrieve_update_counter(request, Videos, VideosSerializer, *args, **kwargs)

    def get_queryset(self):
        queryset = Videos.objects.all()
        tribe = self.request.query_params.get('tribe')
        if tribe is not None:
            queryset = queryset.filter(Tribe_id=tribe)
        return queryset
