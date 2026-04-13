from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
def home(request):
    return render(request, 'website/home.html')  # include the subfolder 'website'

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def project1(request):
    return render(request, 'website/project1.html')

def project2(request):
    return render(request, 'website/project2.html')

def project3(request):
    return render(request, 'website/project3.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                subject=f"New message from {name}",
                message=f"From: {email}\n\nMessage:\n{message}",
                from_email=None,  # uses DEFAULT_FROM_EMAIL
                recipient_list=["contact@basschreurs.nl"],
                fail_silently=False,
            )

            return redirect("contact_success")

    else:
        form = ContactForm()

    return render(request, "website/contact.html", {"form": form})

def contact_success(request):
    return render(request, "website/contact_success.html")