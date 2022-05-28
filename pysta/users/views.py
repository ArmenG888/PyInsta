from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from post.models import post
from .forms import SettingsForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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

@login_required(login_url="/login")
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

@login_required(login_url="/login")
def settings(request):   
    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            themes =(
                ("1", "light"),
                ("2", "dark"),
            )
            theme = form.cleaned_data['theme']
            username = form.cleaned_data['username']
            bio = form.cleaned_data['bio']
            try:
                image = request.FILES['image']
                request.user.profile.image = image
            except Exception:
                pass

            request.user.profile.theme=themes[int(theme)-1][1]
            request.user.profile.bio = bio
            request.user.username = username
            request.user.save()
            request.user.profile.save()
            return redirect('settings')
    else:
        
        form = SettingsForm()

    return render(request, 'users/settings.html', {'form': form})
