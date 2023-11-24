from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from main_page import models
from main_page.api import serializers


class CardViewSet(ModelViewSet):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'




