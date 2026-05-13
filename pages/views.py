from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from quotations.models import Order
from pages.models import Instance, Service

# Create your views here.
def index(request):
    service_items = [
        {
            'title': '水利工程規劃設計',
            'caption': ['水利監測測報工程', '下水道檢監測工程', '土石流監測工程', '河川公地', '水利防災', '水理分析', '水下檢測',
                        '水土保持', '井水水權展延申請', '排水設計', '排水設施改道計劃', '鑽心'],
            'image_url': 'pages/assets/img/services/img1.png',
        },
        {
            'title': '整合防災規劃',
            'caption': ['無人飛機調查', '環境監測工程', '基樁試驗', '防災演練訓練'],
            'image_url': 'pages/assets/img/services/img2.png',
        },
        {
            'title': '土木營建規劃設計',
            'caption': ['大地監(觀)測工程', '橋梁檢測工程', '道路調查', '工程地質'],
            'image_url': 'pages/assets/img/services/img3.png',
        },
    ]
    context = {
        'service_items': service_items
    }
    return render(request, 'pages/index.html', context=context)

def about(request):
    card_items = [
        {
            'title': '基地排水計畫設計',
            'icon_url': 'bi-moisture',
            'url': reverse("pages:service_detail", kwargs={'pk': 1}),
            'contexts': ['流出抑制設施', '透水保水設施', '出流管制', '排水改道', '水土保持', '河川公地申請', '計畫撰寫']
        },
        {
            'title': '透水保水檢查',
            'icon_url': 'bi-droplet-half',
            'url': reverse("pages:service_detail", kwargs={'pk': 2}),
        },
        {
            'title': '水位計安裝',
            'icon_url': 'bi-broadcast',
            'url': reverse("pages:service_detail", kwargs={'pk': 3}),
        },
        {
            'title': '竣工檢查',
            'icon_url': 'bi-clipboard-check',
            'url': '#',
        },
        {
            'title': '透地雷達探測',
            'icon_url': 'bi-activity',
            'url': reverse("pages:service_detail", kwargs={'pk': 5}),
        },
    ]
    case_items = [
        {
            'title': '基地排水計畫設計',
            'count': 68,
        },
        {
            'title': '透水保水檢查',
            'count': 109,
        },
        {
            'title': '水位計安裝',
            'count': 223,
        },
        {
            'title': '竣工查驗',
            'count': 223,
        },
        {
            'title': '透地雷達探測',
            'count': 223,
        },
    ]
    context = {
        'card_items': card_items,
        'case_items': case_items,
    }
    return render(request, 'pages/about.html', context=context)

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
        services =  super().get_queryset()
        return services.filter(is_active=True).order_by('pk')

class ServiceDetailView(generic.DetailView):
    model = Service