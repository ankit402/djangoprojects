from django.shortcuts import render, get_object_or_404
from .models import ChatRoom, ChatMessage
# Create your views here.
def index(request):
    #read db.table data
    chatroom = ChatRoom.objects.all()
    return render(request, 'chatapp/index.html', {'chatroom':chatroom})

def chatroom(request,slug):
   # chatroom= ChatRoom.objects.get(slug=slug)
    chatroom = get_object_or_404(ChatRoom, slug=slug)
    messages = ChatMessage.objects.filter(room = chatroom)[0:30]
    return render(request, 'chatapp/room.html', {'chatroom':chatroom, 'messages':messages})
