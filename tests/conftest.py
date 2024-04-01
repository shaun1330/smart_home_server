import pytest


@pytest.fixture
def user_setup(db):
    from django.contrib.auth.models import User
    user = User.objects.create_user('test_user')
    from rest_framework.authtoken.models import Token
    token = Token.objects.create(user=user)
    yield user, token
    user.delete()


@pytest.fixture
def client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def device_setup(db):
    from devices.models import Device
    device = Device.objects.create(location='Test Location')
    yield device
    device.delete()


