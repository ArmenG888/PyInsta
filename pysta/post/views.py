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

def post_detail_view(request, pk):
    post_x = post.objects.all().filter(id=pk)[0]
    comments = post_x.comment_set.all()
    context = {
        'post':post_x,
        'comments':comments
    }
    return render(request, 'post/post_detail.html', context)