from django.db import models
from django.contrib.auth.models import User

class thread(models.Model):
    from_user = models.ForeignKey(User,related_name="sender",on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name="reciever",on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
class messages(models.Model):
    from_user = models.ForeignKey(User,related_name="from_user",on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name="to_user",on_delete=models.CASCADE)
    text = models.TextField(default="")
    time = models.DateTimeField(auto_now=True)
    thread = models.ForeignKey(thread,default="", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.from_user.username + " to " + self.to_user.username + " " + self.text
    class Meta:
        ordering = ['time']