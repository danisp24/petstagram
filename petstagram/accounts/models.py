from django.db import models

from petstagram.photos.models import Photo


# Create your models here.
class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
