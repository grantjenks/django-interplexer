import subprocess

from django.conf import settings
from django.db import models


class Session(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sessions'
    )

    def __str__(self):
        return f'Session {self.pk} (User: {self.user.username})'

    def _run_tmux_command(self, *args):
        return subprocess.run(
            ['tmux'] + list(args), capture_output=True, check=True, text=True
        )

    def create_tmux_session(self):
        self._run_tmux_command('new-session', '-d', '-s', f'session-{self.pk}')

    def delete_tmux_session(self):
        self._run_tmux_command('kill-session', '-t', f'session-{self.pk}')

    def capture_pane(self):
        result = self._run_tmux_command(
            'capture-pane', '-b', f'session-{self.pk}', '-p'
        )
        return result.stdout

    def send_keys(self, keys):
        self._run_tmux_command(
            'send-keys', '-t', f'session-{self.pk}', *keys.split(' '), 'C-m'
        )

    def save(self, *args, **kwargs):
        new_session = self._state.adding
        super().save(*args, **kwargs)
        if new_session:
            self.create_tmux_session()

    def delete(self, *args, **kwargs):
        self.delete_tmux_session()
        super().delete(*args, **kwargs)
