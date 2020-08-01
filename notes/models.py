from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model


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
        get_user_model(), on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("note", args=[str(self.id), ])
