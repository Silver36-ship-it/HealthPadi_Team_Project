from django.core.mail import send_mail
from django.shortcuts import render

from notification.models import Notification
from providers.models import Providers


# Create your views here.


def create_user_notification(user):
    notification = Notification.objects.create(
        message=f"""
        We are glad to have you here {user.first_name} {user.last_name}!\n   
        Welcome to HealthPadi!   
        """,
    )
    send_mail(
        subject="Welcome to HealthPadi!",
        message=notification.message,
        from_email='',
        recipient_list=[user.email],
        fail_silently=True
    )
    notification.is_read = True
    notification.save()

def create_provider_notification(provider):
    notification = Notification.objects.create(
        message=f"""
        Dear {provider.provider_name}, We are glad to partner with you!
        
        Welcome to HealthPadi!   
        """,
    )
    send_mail(
        subject="Welcome to HealthPadi Partner!",
        message=notification.message,
        from_email='',
        recipient_list=[provider.provider_email],
        fail_silently=True
    )
    notification.is_read = True
    notification.save()

def create_notification_for_provider_views(provider):
    create_user_notification(provider)

