from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math 
class post(models.Model):
    user = models.ForeignKey(User, related_name="post_author", on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField(default="")
    date_posted = models.DateTimeField(default=timezone.now)
    user_liked = models.ManyToManyField(User, related_name="users_liked_post", default="", blank=True)
    views = models.IntegerField(default=0)
    comments = models.ManyToManyField("post.comment", related_name="post_comments", blank=True)
    def time_ago(self):
        now = timezone.now()       
        diff = now - self.date_posted
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds          
            if seconds == 1:
                return str(seconds) +  " second ago"          
            else:
                return str(seconds) + " seconds ago"
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"          
            else:
                return str(minutes) + " minutes ago"
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"
        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days   
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"
        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"
        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"
    class Meta:
        ordering = ['-date_posted']

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