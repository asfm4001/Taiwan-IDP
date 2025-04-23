from django.shortcuts import render
from django.views import generic
from estimates.models import Order

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

class OrdersView(generic.ListView):
    template_name = 'pages/orders.html'
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.all()