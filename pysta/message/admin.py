from django.contrib import admin
from .models import messages,thread

admin.site.register(thread)
admin.site.register(messages)