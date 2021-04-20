from django.shortcuts import redirect, render
from django.conf import settings
from chat.models import PrivateChatRoom, RoomChatMessage

DEBUG = False
# Create your views here.

def private_chat_room_view(request, *args, **kwargs):
    user = request.user

    if not user.is_authenticated:
        return redirect("login")

    context = {}

    context['debug'] = DEBUG
    context['debug_mode'] = settings.DEBUG

    return render(request, "chat/room.html", context)