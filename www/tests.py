import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def user(db):
    return User.objects.create_user('testuser', 'testuser@dummy.com', 'testpassword')


@pytest.fixture
def api_client():
    return APIClient()


def test_access_unauthenticated(api_client):
    url = reverse('session-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_access_authenticated(user, api_client):
    api_client.force_authenticate(user=user)
    url = reverse('session-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_session_workflow(user, api_client):
    api_client.force_authenticate(user=user)

    # Create a new session
    url = reverse('session-list')
    response = api_client.post(url)
    assert response.status_code == status.HTTP_201_CREATED
    new_session_id = response.data['id']

    # Capture the pane
    url = reverse('capture-pane', args=[new_session_id])
    response = api_client.post(url)
    assert response.status_code == status.HTTP_200_OK

    # Send keys to the session
    keys = 'echo hello C-m'
    url = reverse('send-keys', args=[new_session_id])
    response = api_client.post(url, {'keys': keys})
    assert response.status_code == status.HTTP_200_OK

    # Capture the pane to verify keys sent
    url = reverse('capture-pane', args=[new_session_id])
    response = api_client.post(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'hello' in response.data

    # Delete the session
    url = reverse('session-detail', args=[new_session_id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
