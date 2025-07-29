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