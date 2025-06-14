from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    return render(request, 'portfolioapp/home.html')

def projects(request):
    return render(request, 'portfolioapp/projects.html')

def about(request):
    return render(request, 'portfolioapp/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email (make sure your email settings are correct)
            send_mail(
                subject=f"New contact form submission from {name}",
                message=message + f"\n\nFrom: {name} <{email}>",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            messages.success(request, "Your message was sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'portfolioapp/contact.html', {'form': form})
