from skailar.conf import settings
from skailar.db import models


class CustomToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
