from django.db import models

#import for the user
from django.contrib.auth.models import User

# Create your models here.

class GuildInfo(models.Model):
    name = models.CharField(max_length=60)
    ticker = models.CharField(max_length=6)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ParentPost(models.Model):
    posttitle = models.CharField(max_length=150)
    postbody = models.CharField(max_length=1500)
    user = models.ForeignKey(User, default=None)
    
    def __str__(self):
        return self.posttitle


class PostReply(models.Model):
    replybody = models.CharField(max_length=1500)
    user = models.ForeignKey(User, default=None)
