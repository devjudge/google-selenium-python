# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

from django.http import HttpResponse
from rest_framework import status

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from restapi.selenium_service import SeleniumService

logger = logging.getLogger(__name__)


def index():
    return HttpResponse("Hello, world. You're at Rest.")


@api_view(['GET'])
@renderer_classes([JSONRenderer, ])
def get_title(request, format=None):
    """A view that returns google title"""
    title = SeleniumService.get_title_from_google()
    return Response({'response': title}, status=status.HTTP_200_OK)
