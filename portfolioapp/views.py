from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'portfolioapp/home.html')

def projects(request):
    return render(request, 'portfolioapp/projects.html')

def about(request):
    return render(request, 'portfolioapp/about.html')

def contact(request):
    return render(request, 'portfolioapp/contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Example: send email (configure your email settings first)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Simple send mail example (adjust your settings in settings.py)
            send_mail(
                f"New contact form submission from {name}",
                message + f"\n\nFrom: {name} <{email}>",
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],  # Your email to receive messages
            )

            return redirect('contact')  # Redirect after POST to clear form
    else:
        form = ContactForm()

    return render(request, 'portfolioapp/contact.html', {'form': form})
