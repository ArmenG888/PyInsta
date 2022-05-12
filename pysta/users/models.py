from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    following_users = models.ManyToManyField("users.Profile",related_name="users_following", blank=True)
    follower_users = models.ManyToManyField("users.Profile",related_name="users_that_follow", blank=True)
    def __str__(self):
        return self.user.username
    def followers(self):
        return len(self.follower_users.all())
    def following(self):
        return len(self.following_users.all())