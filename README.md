# Open-Chat
Chat web app made in Django.

## Features
1. User Management<br>
    &emspᐅ Registration<br>
    &emspᐅ Login<br>
    &emspᐅ Logout<br>
    &emspᐅ Forgot Password<br>
    &emspᐅ Change Password<br>
    &emspᐅ View accounts<br>
    &emspᐅ Update account properties<br>
    &emspᐅ Search for other users<br>

2. Friend System<br>
    &emspᐅ Send friend requests<br>
    &emspᐅ Accept friend requests<br>
    &emspᐅ Decline friend requests<br>
    &emspᐅ Cancel friend requests<br>
    &emspᐅ Remove Friends<br>

3. Public Chatroom<br>
    &emspᐅ Public chatroom where any authenticated user can chat. (Django Channels & WebSockets)<br>

4. Private Chatroom<br>
    &emspᐅ Have 1-on-1 conversations with friends. (Django Channels and WebSockets)<br>

5. Notifications<br>
    &emspᐅ Real-time notifications for things like:<br>
        &emsp1. Friend requests (Can accept / decline from the notification)<br>
        &emsp2. Private chat messages<br>

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