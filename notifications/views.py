from django.shortcuts import render
from notifications.models import Notification


def note(request, user_id):
    notes = Notification.objects.all()
    unread = Notification.objects.filter(read=False, recipient=request.user)
    for note in unread:
        note.read = True
        note.save()
    return render(request, 'other_user.html', {'notes': notes, 'unread':unread})

def alert(request):
    unread = Notification.objects.filter(read=False, recipient=request.user)
    count = len(unread)
    print(count)
    return render(request, 'base.html', {'unread':unread, 'count': count})
    

