from django.db import models
from django.conf import settings

# Create your models here.
class Session(models.Model):
    session_key = models.CharField(
        max_length=64, 
        unique=True
        )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )
    expire_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.session_key[:6]}"