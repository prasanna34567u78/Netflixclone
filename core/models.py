
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


# Create your models here.

AGE_CHOICES=(
    ('All','All'),
    ('Kids','Kids'),
)
MOVIE_CHOICE=(
    ('seasonal','seasonal'),
    ('singal','singal'),
)

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('profile',blank=True)


class Profile(models.Model):
    name=models.CharField(max_length=210)
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)

#movie table
class Movie(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=20,choices=MOVIE_CHOICE)
    video=models.ManyToManyField('video')
    flyer=models.ImageField(upload_to='flyer')
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)

class Video(models.Model):
    title=models.CharField(max_length=255,blank=True,null=True)
    file=models.FileField(upload_to='movies')