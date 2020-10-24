from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    ''' a model for Project posts '''
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    live_link = models.URLField()
    description = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    ''' extended User model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True, default=f'Hello, I am new here!')
    contacts = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'