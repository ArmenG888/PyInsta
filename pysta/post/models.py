from pydoc import describe
from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    user = models.ForeignKey(User, related_name="post_author", on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField(default="")
    date_posted = models.DateField(auto_now=True)
    user_liked = models.ManyToManyField(User, related_name="users_liked_post", default="", blank=True)
    comments_number = models.IntegerField(default=0)
    def likes(self):
        return len(self.user_liked.all())

    class Meta:
        ordering = ['date_posted'] 

class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comment_author", on_delete=models.CASCADE)
    text = models.TextField(default="")
    user_liked = models.ManyToManyField(User, related_name="users_liked_comment", default="", blank=True)
    def likes(self):
        return len(self.user_liked.all)
 
