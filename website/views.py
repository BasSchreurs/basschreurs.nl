import logging

from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

from .forms import ContactForm

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'website/home.html')  # include the subfolder 'website'

def about(request):
    return render(request, 'website/about.html')

def server_setup(request):
    return render(request, 'website/server_setup.html')

def little_lemon(request):
    return render(request, 'website/little_lemon.html')

def dashboard(request):
    return render(request, 'website/dashboard.html')

def motomeet(request):
    return render(request, 'website/motomeet.html')

def bassinga(request):
    return render(request, 'website/bassinga.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                EmailMessage(
                    subject=f"New message from {name}",
                    body=f"From: {email}\n\n{message}",
                    to=["contact@basschreurs.nl"],
                    reply_to=[email],
                ).send(fail_silently=False)
            except Exception:
                logger.exception("Er ging iets mis")
                form.add_error(None, "Er ging iets mis bij het versturen van uw bericht. Probeer het later opnieuw.")
            else:
                return redirect("contact_success")
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})

def contact_success(request):
    return render(request, "website/contact_success.html")