from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SessionViewSet

router = DefaultRouter()
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'session/<int:pk>/capture-pane/',
        SessionViewSet.as_view({'post': 'capture_pane'}),
        name='capture-pane',
    ),
    path(
        'session/<int:pk>/send-keys/',
        SessionViewSet.as_view({'post': 'send_keys'}),
        name='send-keys',
    ),
]
