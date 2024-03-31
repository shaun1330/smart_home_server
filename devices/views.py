from django.shortcuts import render
from rest_framework.response import Response
import logging
from rest_framework.decorators import api_view
from devices.models import Device

logger = logging.getLogger('server_log')


@api_view(['POST'])
def register_device(request):
    data = request.data
    location = data.get('location')
    device = Device.objects.create(location=location)
    response = {
        'device_id': device.pk
    }
    logger.info(f"Device registered: {device.pk}")
    return Response(response)


@api_view(['POST'])
def heartbeat(request):
    data = request.data
    device_id = data.get('device_id')
    device = Device.objects.get(pk=device_id)
    device.heartbeat()
    response = {
        'device_id': device_id,
        'last_checkin': device.last_checkin
    }
    return Response(response)

