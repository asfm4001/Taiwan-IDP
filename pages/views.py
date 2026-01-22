from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views import generic
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from estimates.models import Order
from pages.email import mailContext
from pages.forms import ContactForm
from pages.models import Instance, Service
import os, json

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
    services = Service.objects.all()
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

def services(request):
    return render(request, 'pages/services.html')

def services_radar(request):
    carousel_items = [
        {
            'image_url': 'pages/assets/img/透地雷達3.png',
            'title': '瑞士PROCEQ-GS9000陣列式透地雷達',
            'caption': '可輕易檢測出路面劣化及沉陷規模及範圍',
        },
        {
            'image_url': 'pages/assets/img/透地雷達1.png',
            'title': 'GS9000操作示意圖',
            'caption': '鋪面劣化檢測',
        },
        {
            'image_url': 'pages/assets/img/透地雷達2.png',
            'title': 'GS9000操作示意圖',
            'caption': '鋪面劣化檢測',
        },
    ]

    context = {
        'carousel_items': carousel_items,
    }
    return render(request, 'pages/radar.html', context=context)

def services_water_retention(request):
    carousel_items = [
        {
            'image_url': 'pages/assets/img/water_retention/img1.png',
            # 'title': '瑞士PROCEQ-GS9000陣列式透地雷達',
            # 'caption': '可輕易檢測出路面劣化及沉陷規模及範圍',
        },
    ]

    context = {
        'carousel_items': carousel_items,
    }
    return render(request, 'pages/water_retention.html', context=context)

def services_water_retention_design(request):
    carousel_items = [
        {
            'image_url': 'pages/assets/img/water_retention/img1.png',
            # 'title': '瑞士PROCEQ-GS9000陣列式透地雷達',
            # 'caption': '可輕易檢測出路面劣化及沉陷規模及範圍',
        },
    ]

    context = {
        'carousel_items': carousel_items,
    }
    return render(request, 'pages/water_retention_design.html', context=context)

def services_water_level_meter(request):
    carousel_items = [
        {
            'image_url': 'pages/assets/img/water_level_meter/demo2.jpg',
            # 'title': '瑞士PROCEQ-GS9000陣列式透地雷達',
            # 'caption': '可輕易檢測出路面劣化及沉陷規模及範圍',
        },
    ]

    context = {
        'carousel_items': carousel_items,
        # 'water_level_meter_pdf': "pages/assets/img/water_level_meter/demo.pdf"
    }
    return render(request, 'pages/water_level_meter.html', context=context)

def cases(request):
    card_items = [
        {
            'image_url': 'pages/assets/img/cases/1.png',
            'card_text': '烏塗社區摸乳巷景觀休憩環境改善工程',
        },
        {
            'image_url': 'pages/assets/img/cases/2.png',
            'card_text': '龍潭區高屏社區茶文化體驗園區營造工程',
        },
        {
            'image_url': 'pages/assets/img/cases/3.png',
            'card_text': '龍潭區大北坑社區客家文化環境綠美化工程',
        },
        {
            'image_url': 'pages/assets/img/cases/1.png',
            'card_text': '林口區後坑溪整治工程',
        },
        {
            'image_url': 'pages/assets/img/cases/2.png',
            'card_text': '德拉楠橋崩塌地復建工程',
        },
        {
            'image_url': 'pages/assets/img/cases/3.png',
            'card_text': '三芝區青山路4.5K復建工程',
        },
        {
            'image_url': 'pages/assets/img/cases/1.png',
            'card_text': '林口區後坑溪整治工程',
        },
        {
            'image_url': 'pages/assets/img/cases/2.png',
            'card_text': '德拉楠橋崩塌地復建工程',
        },
    ]

    context = {
        'card_items': card_items,
    }
    return render(request, 'pages/cases.html', context=context)

def faqs(request):
    return render(request, 'pages/faqs.html')

def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            line_id = form.cleaned_data['line_id']
            services_list = form.cleaned_data['services']
            message = form.cleaned_data['message']
            msg = mailContext(name, phone, email, line_id, services_list, message)
            
            # get target mail list
            target_mails_list = os.getenv("TARGET_EMAIL")
            count = send_mail(
                "台整-客戶諮詢系統通知",
                msg,
                '',
                target_mails_list,
            )
            messages.success(request, '已接收您的訊息，我們將盡快與您聯繫')
            return redirect(reverse('pages:contact'))
        else:
            print("表單錯誤: ", form.errors)
            print(form.errors.as_json())
    
    form = ContactForm()
   
    context = {'form': form,}
    return render(request, 'pages/contact.html', context=context)

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

class ServiceDetailView(generic.DetailView):
    model = Service