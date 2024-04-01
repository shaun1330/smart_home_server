
def test_register_device(client, user_setup):
    user, token = user_setup
    response = client.post(
        '/api/devices/register',
        {'location': 'Test Location'},
        format='json',
        headers={'Authorization': f'Token {token.key}'}
    )
    assert response.status_code == 200
    assert response.data['location'] == 'Test Location'


def assert_datetime_format(datetime_str):
    import re
    assert re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', datetime_str)


def test_heartbeat(client, user_setup, device_setup):
    device = device_setup
    user, token = user_setup
    response = client.post(
        '/api/devices/heartbeat',
        {'device_id': device.pk},
        format='json',
        headers={'Authorization': f'Token {token.key}'}
    )
    assert response.status_code == 200
    assert 'last_checkin' in response.data
    last_checkin = response.data['last_checkin']
    assert_datetime_format(last_checkin)
