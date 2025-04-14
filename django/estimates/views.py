from django.shortcuts import render
from django.views import generic
from .models import Order

# Create your views here.
def index(request):
    return render(request, 'estimates/index.html')

class DetailView(generic.DetailView):
    for order in Order.objects.all():
        order.order_amount = order.calculate_total_amount()
    model = Order
    template_name = 'estimates/detail.html'
