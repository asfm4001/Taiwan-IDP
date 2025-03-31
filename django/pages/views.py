from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def cases(request):
    return render(request, 'pages/cases.html')

def faqs(request):
    return render(request, 'pages/faqs.html')

def contact(request):
    return render(request, 'pages/contact.html')