from django.db import models
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    subject = models.CharField(max_length=50, blank=True)
    sub_subject = models.CharField(max_length=50, blank=True)
    priority_choices = [
        ('High', 'High'),
        ('Normal', 'Normal'),
        ('Low', 'Low'),
    ]
    priority = models.CharField(
        max_length=10, choices=priority_choices, default='Normal')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
