from django.db import models
from django.contrib.auth.models import User
import PIL.Image

# Create your models here.
class Post(models.Model):
    ''' a model for Project posts '''
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    live_link = models.URLField()
    description = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news


class Profile(models.Model):
    ''' extended User model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.png', upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True, default=f'Hello, I am new here!')
    contacts = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = PIL.Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)        