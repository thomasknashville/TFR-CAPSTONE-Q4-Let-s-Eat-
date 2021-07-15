from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from users.models import TFRUser
from notifications.models import Notification


# Create your views here.


def note(request, user_id):
    notes = Notification.objects.all()
    unread = Notification.objects.filter(read=False, recipient=request.user)
    for note in unread:
        note.read = True
        note.save()
    return render(request, 'other_user.html', {'notes': notes, 'unread':unread})
