from django.shortcuts import render
from django.views import generic
from django.template.loader import select_template
from django.http import Http404
from quotations.models import Order
from pages.models import Instance, Service
from pages.data.indexs import SERVICE_ITEMS
from pages.data.services import SERVICES
from pages.data.abouts import CARD_ITEMS, CASE_ITEMS
from pages.data.service_details import SERVICE_DETAILS

# Create your views here.
def index(request):
    context = {
        'service_items': SERVICE_ITEMS
    }
    return render(request, 'pages/index.html', context=context)

def about(request):
    context = {
        'card_items': CARD_ITEMS,
        'case_items': CASE_ITEMS,
    }
    return render(request, 'pages/about.html', context=context)

def services(request):
    context = {
        'services': SERVICES,
    }
    return render(request, 'pages/services.html', context)

def service_detail(request, slug):
    service = SERVICE_DETAILS.get(slug)

    if not service:
        raise Http404("Service not found")
    
    template = select_template([f"pages/services/service_{slug}.html", ])

    return render(request, template.template.name, context=service)

def contact(request):
    return render(request, 'pages/contact.html')

class OrdersView(generic.ListView):
    template_name = 'pages/orders.html'
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.all()

class InstanceListView(generic.ListView):
    model = Instance

    def get_context_data(self, **kwargs):
        carousel_items = [
            {
                'image_url': 'pages/assets/img/instance/water_retention_instance_v4.jpg',
                # 'title': '瑞士PROCEQ-GS9000陣列式透地雷達',
                # 'caption': '可輕易檢測出路面劣化及沉陷規模及範圍',
            },
        ]
        context =  super().get_context_data(**kwargs)
        context['carousel_items'] = carousel_items
        # context['water_retention_pdf'] = "pages/assets/img/instance/water_retention_instance_v4.pdf"
        return context

class ServiceListView(generic.ListView):
    model = Service
    
    def get_queryset(self):
        return Service.filter(is_active=True).order_by('pk')

class ServiceDetailView(generic.DetailView):
    model = Service