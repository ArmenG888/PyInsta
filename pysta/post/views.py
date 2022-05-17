from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import post, comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile
from .forms import PostForm
import os

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
        'posts':posts_users_follows,
    }

    return render(request, 'post/home.html', context)


def welcome_page(request):
    return render(request, 'post/welcome_page.html')

@login_required(login_url="/admin")
def explore(request):
    context = {
        'posts':post.objects.all()
    }
    return render(request, 'post/explore.html', context)

@login_required(login_url="/admin")
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

@login_required(login_url="/admin")
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

    return HttpResponse('<script>history.back();</script>')

@login_required(login_url="/admin")
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

@login_required(login_url="/admin")   
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

@login_required(login_url="/admin")
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            description = form.cleaned_data['description']
            image = request.FILES['image']
            print(image)
            p = post(user=user, description=description, image=image)
            p.save()
            
            return redirect('post-detail', p.id)
    else:
        form = PostForm()

    return render(request, 'post/create_post.html', {'form': form})

@login_required(login_url="/admin")
def delete_post(request, post_id):
    post_to_delete = post.objects.all().filter(id=post_id)
    os.remove(post_to_delete.image.url)
    post_to_delete.delete()
<<<<<<< Updated upstream
    return redirect('home')
=======
    messages.success(request, "Successfully deleted your post")
    return redirect('home')

>>>>>>> Stashed changes
