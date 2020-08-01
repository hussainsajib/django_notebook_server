from django.db import models
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    subject = models.CharField(max_length=50)
    sub_subject = models.CharField(max_length=50)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
