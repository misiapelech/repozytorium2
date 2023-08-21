from django.contrib.auth.models import User
from django.test import Client
import pytest

@pytest.fixture
def authenticated_client():
    """Fixture providing a logged-in test client."""
    User.objects.create_user(username='testuser', password='testpassword')
    client = Client()
    client.login(username='testuser', password='testpassword')
    return client