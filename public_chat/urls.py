from django.urls import path

from public_chat.views import(
    public_chat_view,
)

app_name = 'public_chat'

urlpatterns = [
    path('<room_id>/', public_chat_view, name='view'),
]