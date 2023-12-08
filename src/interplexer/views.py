import subprocess

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Session
from .serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def capture_pane(self, request, pk=None):
        session = self.get_object()
        try:
            output = session.capture_pane()
            return Response(output, content_type='text/plain')
        except subprocess.CalledProcessError as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['post'])
    def send_keys(self, request, pk=None):
        session = self.get_object()
        keys = request.data.get('keys', '')
        try:
            session.send_keys(keys)
            return Response(
                {'detail': 'Keys sent successfully'}, status=status.HTTP_200_OK
            )
        except subprocess.CalledProcessError as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
