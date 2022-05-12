from django.shortcuts import render, redirect
from .models import post, comment
from django.contrib.auth.decorators import login_required


@login_required(login_url="/admin")
def home(request):
    for i in post.objects.all():
        comments = i.comment_set.all()
        i.comments_number = len(comments)
        i.comments.set(comments)
        i.likes = i.likess()
        i.save()
    posts_users_follows = []
    for i in post.objects.all():
        if i.user.profile in request.user.profile.following_users.all():
            posts_users_follows.append(i)

    context = {
        'posts':posts_users_follows
    }

    return render(request, 'post/home.html', context)

def post_detail_view(request, id):
    post_x = post.objects.all().filter(id=id)[0]
    post_x.views += 1
    post_x.save()
    comments = post_x.comment_set.all()
    for comment in comments:
        replys = comment.reply_set.all()
        comment.replys.set(replys)
        comment.save()
    for i in post_x.comment_set.all():
        i.likes = i.likess()
        i.save()
    comments = post_x.comment_set.all()  
    context = {
        'post':post_x,
        'comments':comments
    }
    return render(request, 'post/post_detail.html', context)

def like(request, id):
    post_x = post.objects.all().filter(id=id)[0]
    already_liked = False 
    for i in post_x.user_liked.all():
        if i == request.user:
            already_liked = True 
    
    if already_liked == False:
        post_x.user_liked.add(request.user)
    else:
        post_x.user_liked.remove(request.user)

    return redirect('home')

def like_detail(request, id):
    post_x = post.objects.all().filter(id=id)[0]
    already_liked = False 
    for i in post_x.user_liked.all():
        if i == request.user:
            already_liked = True 
    
    if already_liked == False:
        post_x.user_liked.add(request.user)
    else:
        post_x.user_liked.remove(request.user)

    return redirect('post-detail', id)
    
def comment_like(request, id, comment_id):
    comment_x = comment.objects.all().filter(id=comment_id)[0]
    post_x = comment.objects.all().filter(id=id)[0]
    already_liked = False 
    for i in comment_x.user_liked.all():
        if i == request.user:
            already_liked = True 
    
    if already_liked == False:
        comment_x.user_liked.add(request.user)
    else:
        comment_x.user_liked.remove(request.user)
    

    return redirect('post-detail', id) 