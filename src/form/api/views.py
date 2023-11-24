from rest_framework.viewsets import ModelViewSet

from rest_framework import status
from rest_framework.response import Response

from form import models
from form.utils.telegram_bot_util import TelegramBot
from form.api import serializers
from form.api.decorators import range_limit


class FormViewSet(ModelViewSet):
    queryset = models.Form.objects.all()
    serializer_class = serializers.FormSerializer

    @range_limit(4, 3600)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        TelegramBot.telegram_bot_sender(
            request, serializer
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DropDownViewSet(ModelViewSet):
    queryset = models.DropDownSide.objects.all()
    serializer_class = serializers.DropDownSerializer
