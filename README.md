# Open-Chat
Chat web app made in Django.

## Features
1. User Management
    ᐅ Registration
    ᐅ Login
    ᐅ Logout
    ᐅ Forgot Password
    ᐅ Change Password
    ᐅ View accounts
    ᐅ Update account properties
    ᐅ Search for other users

2. Friend System
    ᐅ Send friend requests
    ᐅ Accept friend requests
    ᐅ Decline friend requests
    ᐅ Cancel friend requests
    ᐅ Remove Friends

3. Public Chatroom
    ᐅ Public chatroom where any authenticated user can chat. (Django Channels & WebSockets)

4. Private Chatroom
    ᐅ Have 1-on-1 conversations with friends. (Django Channels and WebSockets)

5. Notifications
    ᐅ Real-time notifications for things like:
        1. Friend requests (Can accept / decline from the notification)
        2. Private chat messages

## Getting Started
This project is made on **Python 3.8.9** and **Django 2.2.19**.

Install required depedencies:
```
pip install requirements.txt
```

Run following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```