from django.shortcuts import render
from django.conf import settings

from public_chat.models import PublicChatRoom

DEBUG = False

def public_chat_view(request, room_id):

    room = PublicChatRoom.objects.get(id = room_id)

    context = {}
    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG
    context['room_id'] = room_id
    context['room'] = room

    return render(request, f"public_chat/public_chat_rooms.html", context)