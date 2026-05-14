from django.urls import reverse_lazy
CARD_ITEMS = [
    {
        'title': '基地排水計畫設計',
        'icon_url': 'bi-moisture',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'design'}),
        'contexts': ['流出抑制設施', '透水保水設施', '出流管制', '排水改道', '水土保持', '河川公地申請', '計畫撰寫']
    },
    {
        'title': '透水保水檢查',
        'icon_url': 'bi-droplet-half',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'inspection'}),
    },
    {
        'title': '水位計安裝',
        'icon_url': 'bi-broadcast',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'meter'}),
    },
    {
        'title': '竣工檢查',
        'icon_url': 'bi-clipboard-check',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'completion'}),
    },
    {
        'title': '透地雷達探測',
        'icon_url': 'bi-activity',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'radar'}),
    },
]

CASE_ITEMS = [
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