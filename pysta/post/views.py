from django.shortcuts import render
from .models import post, comment
def home(request):
    for i in post.objects.all():
        comments = i.comment_set.all()
        i.comments_number = len(comments)
        i.save()
    context = {
        'posts':post.objects.all()
    }

    return render(request, 'post/home.html', context)
