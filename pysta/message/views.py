from django.shortcuts import redirect, render
from .models import thread,messages
from django.db.models import Q
from .forms import MessageForm
def threads(request):
    user = request.user
    threads = thread.objects.filter(Q(from_user=request.user) | Q(to_user=request.user))
    print(threads)
    for i in threads:
        messages = i.messages_set.all()
        print(messages)
    return render(request, "message/all_user_messages.html", {'threads':threads})

def direct_messages(request,id):
    thread_x = thread.objects.filter(id=id)[0]
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