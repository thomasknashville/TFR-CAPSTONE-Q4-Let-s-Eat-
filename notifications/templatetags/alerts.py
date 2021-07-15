from django import template
from notifications.models import Notification
from django.shortcuts import render
from django.template.loader import get_template

register = template.Library()

def show_alerts(user):
    unread = Notification.objects.filter(read=False, recipient=user)
    alerts = unread.count
    print(unread)
    return {'alerts': alerts}

base_template = get_template('base.html')
register.inclusion_tag(base_template)(show_alerts)