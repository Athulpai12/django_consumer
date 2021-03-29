from django.core.mail import send_mail
from basic_view import consumer

from django.core import serializers

def send_email(email_list):
    try:
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            email_list,
            fail_silently=False,
        )


    except Exception:
        # exponentail back off with retry
        pass