from django.db import models
from django.contrib.auth.models import User
import PIL.Image
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    ''' a model for Project posts '''
    title = models.CharField(max_length=150)
    image = CloudinaryField('image')
    live_link = models.URLField()
    description = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    @classmethod
    def search_by_title(cls,search_term):
        found_projects = cls.objects.filter(title__icontains=search_term)
        return found_projects


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

class Rating(models.Model):
    ''' model to allow users to rate post on three categories '''
    Rating_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
    )
    interface = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    experience = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    content = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post}'s rating"

    def save_rating(self):
        ''' method to save ratings '''
        self.save()

    def delete_rating(self):
        ''' method to delete ratings '''
        self.delete()


