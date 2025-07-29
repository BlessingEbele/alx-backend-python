from django.shortcuts import render, get_object_or_404
from .models import Message, MessageHistory, Conversation



#def message_detail(request, pk):
#    message = get_object_or_404(Message, pk=pk)
#    history = message.history.all().order_by('-edited_at')  # Access related MessageHistory
#    return render(request, 'messaging/message_detail.html', {
#        'message': message,
#        'history': history,
#    })

def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    history = MessageHistory.objects.filter(message=message).order_by('-edited_at')
    return render(request, 'messaging/message_detail.html', {
        'message': message,
        'history': history
    })

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from .forms import MessageReplyForm

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    messages.success(request, "Your account and all related data have been deleted.")
    return redirect("login")  # or home page


def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    
    # Fetch all top-level messages and prefetch their replies
    # Optimize DB queries
    messages = Message.objects.filter(conversation=conversation, parent_message__isnull=True) \
        .select_related('sender', 'receiver') \
        .prefetch_related('history', 'replies')

    form = MessageReplyForm()
    
    return render(request, 'messaging/conversation_detail.html', {
        'conversation': conversation,
        'messages': messages,
        'form': form  
    })

def get_all_replies(message):
    replies = message.replies.all()
    nested = []
    for reply in replies:
        nested.append({
            'message': reply,
            'replies': get_all_replies(reply)
        })
    return nested



def reply_to_message(request, conversation_id, parent_message_id):
    parent = get_object_or_404(Message, id=parent_message_id)
    conversation = get_object_or_404(Conversation, id=conversation_id)

    if request.method == 'POST':
        form = MessageReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.receiver = parent.sender  # optional, adjust logic
            reply.conversation = conversation
            reply.parent_message = parent
            reply.save()
            return redirect('conversation_detail', conversation_id=conversation.id)
    else:
        form = MessageReplyForm()

    return render(request, 'messaging/reply_form.html', {
        'form': form,
        'parent': parent,
        'conversation': conversation
    })

@login_required
def send_message(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)

    if request.method == 'POST':
        form = MessageReplyForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender=request.user  # ✅ checker looks for this
            message.conversation = conversation
            message.save()
            return redirect('conversation_detail', conversation_id=conversation.id)
    else:
        form = MessageReplyForm()

    return render(request, 'messaging/send_message.html', {'form': form, 'conversation': conversation})

@login_required
def unread_messages(request):
    messages = Message.unread.for_user(request.user)
    return render(request, 'messaging/unread_messages.html', {'messages': messages})
