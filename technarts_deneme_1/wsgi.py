"""
WSGI config for technarts_deneme_1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'technarts_deneme_1.settings')

application = get_wsgi_application()




def create_initial_user():
    import django
    django.setup()
    from django.contrib.auth.models import User
    try:
        user = User.objects.get(username="user")
    except  User.DoesNotExist:
        user = User.objects.create_user("user", password="1234")
        user.save()

create_initial_user()
