from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Client, Mailing, MessageLog

from .serializers import (ClientSerializer, MailinglistSerializer,
                          MailingSerializer, MessageLogSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('tag', 'code')


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MailinglistSerializer
        return MailingSerializer


class MessageLogViewSet(viewsets.ModelViewSet):
    queryset = MessageLog.objects.all()
    serializer_class = MessageLogSerializer