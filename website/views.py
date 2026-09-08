from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
def home(request):
    return render(request, 'website/home.html')  # include the subfolder 'website'

def about(request):
    return render(request, 'website/about.html')

def little_lemon(request):
    return render(request, 'website/little_lemon.html')

def dashboard(request):
    return render(request, 'website/dashboard.html')

def motomeet(request):
    return render(request, 'website/motomeet.html')

def bassinga(request):
    return render(request, 'website/bassinga.html')

def lorum_ipsum(request):
    return render(request, 'website/lorum_ipsum.html')

def contact_view(request):
    print("VIEW HIT")

    if request.method == "POST":
        print("POST HIT")

        form = ContactForm(request.POST)

        print("FORM CREATED")

        if form.is_valid():
            print("FORM IS VALID")

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"New message from {name}",
                message=f"From: {email}\n\n{message}",
                from_email=None,
                recipient_list=["contact@basschreurs.nl"],
                fail_silently=False,
            )

            print("EMAIL SENT")

            return redirect("contact_success")

        else:
            print("FORM INVALID:", form.errors)

    return render(request, "website/contact.html", {"form": ContactForm()})

def contact_success(request):
    return render(request, "website/contact_success.html")