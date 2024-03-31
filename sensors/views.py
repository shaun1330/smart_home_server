from django.shortcuts import render
from rest_framework.response import Response
import logging
from rest_framework.decorators import api_view

logger = logging.getLogger(__name__)

@api_view(['GET'])
def index(request):
    data = {
        'name': 'Django REST framework',
    }
    logger.info('Hello, Django!')
    return Response(data)


