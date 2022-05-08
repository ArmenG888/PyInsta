from django.contrib import admin
from .models import post,comment,reply

admin.site.register(post)
admin.site.register(comment)
admin.site.register(reply)