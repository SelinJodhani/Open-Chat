# Open-Chat
Chat web app made in Django.

## Features
1. User Management<br>
    ᐅ Registration<br>
    ᐅ Login<br>
    ᐅ Logout<br>
    ᐅ Forgot Password<br>
    ᐅ Change Password<br>
    ᐅ View accounts<br>
    ᐅ Update account properties<br>
    ᐅ Search for other users<br>

2. Friend System<br>
    ᐅ Send friend requests<br>
    ᐅ Accept friend requests<br>
    ᐅ Decline friend requests<br>
    ᐅ Cancel friend requests<br>
    ᐅ Remove Friends<br>

3. Public Chatroom<br>
    ᐅ Public chatroom where any authenticated user can chat. (Django Channels & WebSockets)<br>

4. Private Chatroom<br>
    ᐅ Have 1-on-1 conversations with friends. (Django Channels and WebSockets)<br>

5. Notifications<br>
    ᐅ Real-time notifications for things like:<br>
        1. Friend requests (Can accept / decline from the notification)<br>
        2. Private chat messages<br>

## Getting Started
This project is made on **Python 3.8.9** and **Django 2.2.19**.

#### Install required depedencies:
```
pip install requirements.txt
```

#### Run following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```