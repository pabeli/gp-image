from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    # This field will store the image
    image = models.BinaryField(blank=True)
    mime_type = models.CharField(max_length=500, default='jpeg')