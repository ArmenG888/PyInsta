from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class post(models.Model):
    user = models.ForeignKey(User, related_name="post_author", on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField(default="")
    date_posted = models.DateTimeField(default=timezone.now)
    user_liked = models.ManyToManyField(User, related_name="users_liked_post", default="", blank=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    comments_number = models.IntegerField(default=0)
    comments = models.ManyToManyField("post.comment", related_name="post_comments")
    def likess(self):
        return len(self.user_liked.all())
    class Meta:
        ordering = ['-likes','-views','-comments_number','-date_posted']

class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comment_author", on_delete=models.CASCADE)
    text = models.TextField(default="")
    user_liked = models.ManyToManyField(User, related_name="users_liked_comment", default="", blank=True)
    likes = models.IntegerField(default=0)
    replys = models.ManyToManyField("post.reply", related_name="comment_replys", default="", blank=True)
    def replys_num(self):
        return len(self.replys.all())
    def likess(self):
        return len(self.user_liked.all())
    
    class Meta:
        ordering = ['-likes']
class reply(models.Model):
    comment = models.ForeignKey(comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reply_author", on_delete=models.CASCADE)
    text = models.TextField(default="")