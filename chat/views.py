from django import conf
from django.shortcuts import redirect, render
from django.conf import settings
from chat.models import PrivateChatRoom, RoomChatMessage
from itertools import chain

DEBUG = False
# Create your views here.

def private_chat_room_view(request, *args, **kwargs):
    user = request.user

    if not user.is_authenticated:
        return redirect("login")

    # 1. Find all the rooms this user is part of.
    rooms1 = PrivateChatRoom.objects.filter(user1=user, is_active=True)
    rooms2 = PrivateChatRoom.objects.filter(user2=user, is_active=True)

    # 2. Merge the lists
    rooms = list(chain(rooms1, rooms2))

    # m_and_f
    # [{'message': 'hey', 'friend': 'Selin'}, {'message': 'You there?', 'friend': 'Meet'}]
    m_and_f = []

    for room in rooms:
        # Figure out which user is the ohther user (aka friend)
        
        if room.user1 == user:
            friend = room.user2
        else:
            friend = room.user1

        m_and_f.append({
            "message": "",
            "friend": friend
        })

    context = {}

    context['debug'] = DEBUG
    context['debug_mode'] = settings.DEBUG
    context['m_and_f'] = m_and_f

    return render(request, "chat/room.html", context)