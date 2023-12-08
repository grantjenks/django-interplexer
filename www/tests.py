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
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_access_authenticated(user, api_client):
    api_client.force_authenticate(user=user)
    url = reverse('session-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
