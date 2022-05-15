from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from post.models import post


def public_profile(request, username):
    user = get_object_or_404(User, username=username)
    following = False
    if request.user.profile in user.profile.follower_users.all():
        following = True
    context = {
        'posts':post.objects.filter(user=request.user),
        'profile' : user, 
        'following': following
    }

    return render(request, 'users/public_profile.html', context)

def follow(request, username):
    user = get_object_or_404(User, username=username)
    user.profile.follower_users.add(request.user.profile)
    user.profile.followers = len(user.profile.follower_users.all())
    user.save()

    request_user = request.user
    request_user.profile.following_users.add(user.profile)
    request_user.profile.following = len(request_user.profile.following_users.all())
    request_user.save()
    return redirect('public_profile', username=username)
def unfollow(request, username):
    user = get_object_or_404(User, username=username)
    user.profile.follower_users.remove(request.user.profile)
    user.profile.followers = len(user.profile.follower_users.all())
    user.save()
    request_user = request.user
    request_user.profile.following_users.remove(user.profile)
    request_user.profile.following = len(request_user.profile.following_users.all())
    request_user.save()
    return redirect('public_profile', username=username)