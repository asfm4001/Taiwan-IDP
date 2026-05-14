from django.urls import reverse_lazy
from pages.data import shapes

SERVICES = [
    {
        'icon_color': 'cyan',
        'shape': shapes.DESIGN,
        'icon': 'moisture',
        'title': '基地排水計畫設計',
        'desc': '專業承辦各類透水保水與排水設計業務，涵蓋新北市透水保水計畫、新北出流管制、台北市流出抑制、水土保持設施排水設計及排水設施改道規劃等項目。協助建案符合法規要求，優化雨水滯洪與排放設計，降低都市淹水風險，提升基地開發效能與審查通過率。',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'design'}),
    },
    {
        'icon_color': 'orange',
        'shape': shapes.INSPECTION,
        'icon': 'droplet-half',
        'title': '透水保水檢查',
        'desc': '透水保水設施檢查是針對都市開發區或建築基地內所設置的透水性地面與保水結構，進行定期檢視與維護的作業。其主要目的是確保設施能正常發揮滲透雨水、減少地表逕流、補注地下水與調節都市熱島效應等功能。',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'inspection'}),
    },
    {
        'icon_color': 'red',
        'shape': shapes.METER,
        'icon': 'broadcast',
        'title': '水位計安裝',
        'desc': '採用先進雷達技術進行非接觸式水位測量，實現高精度、即時監測。設備穩定可靠，耐候性強，適用於河川、水庫、排水系統及各類水利土木工程現場。透過智能化數據收集與分析，協助工程管理者掌握水位變化，提升防洪、排水及水資源調度效率，確保工程安全運行，實現精準管理與長期可靠監控。',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'meter'}),
    },
    {
        'icon_color': 'teal',
        'shape': shapes.COMPLETION,
        'icon': 'clipboard-check',
        'title': '竣工查驗',
        'desc': '...',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'completion'}),
    },
    {
        'icon_color': 'gray',
        'shape': shapes.RADAR,
        'icon': 'activity',
        'title': '透地雷達探測',
        'desc': '透地雷達儀（Ground Penetrating Radar, GPR），簡高頻脈波（電磁波）射入地下或建築結構體內，在室內經資料處理後，則可作為分析研判探測物的內部構造。於實際應用時以雷達波射入地下或建築結構體內，來推測地下地層的起伏、描繪地下地形地物的形貌及偵檢地下人為或天然的構造體（例如瀝青鋪面厚度、地下管線或空洞、掩埋古蹟、地底孔隙、基礎等）或非金屬構造體之內部結構（如水泥混凝土牆版內的鋼筋，混凝土中之裂隙等）。',
        'url': reverse_lazy("pages:service_detail", kwargs={'slug': 'radar'}),
    },
]