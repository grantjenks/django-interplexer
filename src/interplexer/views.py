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

    @action(detail=True, methods=['post'])
    def capture_pane(self, request, pk=None):
        session = self.get_object()
        try:
            output = subprocess.check_output(
                ['tmux', 'capture-pane', '-b', f'session-{session.id}', '-p']
            ).decode('utf-8')
        except subprocess.CalledProcessError as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(output, content_type='text/plain')

    @action(detail=True, methods=['post'])
    def send_keys(self, request, pk=None):
        session = self.get_object()
        keys = request.data.get('keys', '')
        try:
            subprocess.run(
                ['tmux', 'send-keys', '-t', f'session-{session.id}', keys, 'C-m']
            )
        except subprocess.CalledProcessError as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'detail': 'Keys sent successfully'}, status=status.HTTP_200_OK)
