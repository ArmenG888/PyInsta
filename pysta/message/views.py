from django.shortcuts import redirect, render
from .models import thread,messages
from django.db.models import Q
from .forms import MessageForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def threads(request):
    users = []
    for i in request.user.profile.following_users.all():
        if i in request.user.profile.follower_users.all() and i.user != request.user:
            print(i)
            users.append(i.user)
    return render(request, "message/all_user_messages.html", {'users':users})

@login_required(login_url="/login")
def new_chat(request, username):
    user = User.objects.filter(username=username)
    threads = thread.objects.filter( Q(from_user=user) | Q(from_user=request.user))[0]
    print(threads)

@login_required(login_url="/login")
def direct_messages(request,id):
    thread_x = thread.objects.filter(id=id)[0]
    thread_x.read = True
    thread_x.save()
    if thread_x.from_user == request.user:
        to_user = thread_x.to_user
    else:
        to_user = thread_x.from_user

    messages = thread_x.messages_set.all()
    if request.method == 'POST':
        messageform = MessageForm(request.POST)
        if messageform.is_valid():
            messages.create(from_user=request.user, to_user=to_user, text=messageform.cleaned_data['text'], thread=thread_x)
            return redirect('direct-messages',id=id)
    else:
        messageform = MessageForm()
    return render(request, "message/messages.html", {'direct_messages':messages,'messageform':messageform})