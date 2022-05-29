from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    followers = models.IntegerField(default=0)
    following_users = models.ManyToManyField("users.Profile",related_name="users_following", blank=True)
    follower_users = models.ManyToManyField("users.Profile",related_name="users_that_follow", blank=True)
    theme = models.CharField(default="light", max_length=10)
    bio = models.TextField(default="")
    def __str__(self):
        return self.user.username
    def followerss(self):
        return len(self.follower_users.all())
    def following(self):
        return len(self.following_users.all())

    class Meta:
        ordering = ['-followers']