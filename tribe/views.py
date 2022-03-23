from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Tribes, Rockstars, Articles, OnDemandRequests
from .serializers import TribesSerializer, RockstarsSerializer, ArticlesSerializer, OnDemandRequestsSerializer


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


class OnDemandRequestsViewSet(
    GenericViewSet
):
    serializer_class = OnDemandRequestsSerializer
    queryset = OnDemandRequests.objects.all()

    def create(self, request):
        # Fetch data from POST
        name = request.data['name']
        phone_number = request.data['phone_number']
        date = request.data['date']
        subject = request.data['subject']

        # Create entry in db
        OnDemandRequests.objects.create(PhoneNumber=phone_number, Date=date, Subject=subject)

        # Render template
        context = {'name': name, 'date': date}
        html_message = render_to_string('mail_template/RockstarEmailConfirmation.html', context)
        plain_message = strip_tags(html_message)

        to = ['rockstarsdjangobackend@gmail.com']
        subject = 'Requested Speaker'
        send_mail(subject=subject, message=plain_message, html_message=html_message, recipient_list=to,
                  from_email=None)  # Use default from e-mail and allow plain text message where HTML is unsupported

        return Response(None)
