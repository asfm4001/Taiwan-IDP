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

from django_weasyprint import WeasyTemplateResponse

def pdf(request, order_no):
    order = Order.objects.filter(pk=order_no).first()
    context = {'order': order,}

    response = WeasyTemplateResponse(
        request=request,
        template='estimates/detail.html',   # html模板
        context=context,
        filename='report.pdf',         # 'report.pdf'預設為自動下載
        attachment=True
        # stylesheets=['pages/static/pages/assets/css/estimate.css'],   # 獨立css
    )
    return response