from django.shortcuts import render, get_object_or_404
from .models import Message, MessageHistory



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

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    messages.success(request, "Your account and all related data have been deleted.")
    return redirect("login")  # or home page
