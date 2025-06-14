from django.shortcuts import render, redirect, get_object_or_404
from .models import GuestbookMessage
from .forms import GuestbookForm

def guestbook_view(request):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
    else:
        form = GuestbookForm()

    entries = GuestbookMessage.objects.order_by('-created_at')
    return render(request, 'guestbook/guestbook.html', {
        'form': form,
        'entries': entries,
    })

def delete_message(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(GuestbookMessage, pk=message_id)
        message.delete()
    return redirect('guestbook')

