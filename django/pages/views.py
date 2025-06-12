from django.shortcuts import render
from django.views import generic
from estimates.models import Order

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
            'title': '結構安全鑑定',
            'caption': '安全鑑定以標的物之結構體的安全與否為首要目的',
            'icon_url': 'bi-house-exclamation',
        },
        {
            'title': '建築物耐震能力',
            'caption': '初步、詳細評估 補強設計與監造',
            'icon_url': 'bi-building',
        },
        {
            'title': '道路、橋梁、公園、景觀工程',
            'caption': '工程設計與監造',
            'icon_url': 'bi-tree',
        },
        {
            'title': '水土保持、野溪整治工程',
            'caption': '工程設計與監造',
            'icon_url': 'bi-rulers',
        },
    ]
    case_items = [
        {
            'title': '水利工程案例',
            'count': 68,
        },
        {
            'title': '環境景觀規劃案例',
            'count': 109,
        },
        {
            'title': '土木營建規劃案例',
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
    form = {
        'services': ['水利監測測報工程', '下水道檢監測工程', '土石流監測工程', '無人飛機調查', '環境監測工程', '基樁試驗',
                      '防災演練訓練', '大地監(觀)測工程', '橋梁檢測工程', '道路調查', '工程地質']
    }
    context = {
        'form': form
    }
    return render(request, 'pages/contact.html', context=context)

class OrdersView(generic.ListView):
    template_name = 'pages/orders.html'
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.all()