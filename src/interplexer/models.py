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
