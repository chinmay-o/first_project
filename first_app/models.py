from django.db import models
from django.contrib.auth.models import User as UserCred

# Create your models here.
class Topic(models.Model):

    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):

        return self.top_name

class Webpage(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):

        return self.name

class AccessLog(models.Model):

    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):

        return str(self.date)

class User(models.Model):

    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)

    def __str__(self):

        name = self.first_name + " " + self.last_name
        return name

class UserProfileInfo(models.Model):

    user = models.OneToOneField(UserCred, on_delete=models.CASCADE)

    url = models.URLField(blank = True)

    def __str__(self):

        return self.user.username
