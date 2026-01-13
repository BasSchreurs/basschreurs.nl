from django.shortcuts import render

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