from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PlayList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)  # ToDo: turn this to a url
    date_added = models.DateTimeField("date added")
    last_checked = models.DateTimeField("last checked")

    def __str__(self):
        return self.name


class Video(models.Model):
    playlist = models.ForeignKey(PlayList, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)  # ToDo: turn this to a url
    still_exist = models.BooleanField(default=True)

    def __str__(self):
        return self.name


























