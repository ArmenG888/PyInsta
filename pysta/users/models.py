from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')