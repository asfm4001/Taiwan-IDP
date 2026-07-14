# Project Structure 專案架構
```plaintext
pages/
├── views.py            # 頁面邏輯
├── urls.py             # URL 路由
├── forms.py            # 表單
├── models.py           # 資料模型
├── tests.py            # 單元測試
├── templates/          # HTML 模板
├── static/             # CSS、JavaScript、圖片
└── data/               # 靜態資料
```

# URLs 路由
| 路由 (URL) | 頁面 |
|------------|------|
| `/` | 首頁 |
| `/about/` | 關於我們 |
| `/services/` | 技術服務 |
| `/services/design/` | 基地排水計畫設計 |
| `/services/inspection/` | 透水保水檢查 |
| `/services/meter/` | 水位計安裝 |
| `/services/completion/` | 竣工查驗 |
| `/services/radar/` | 透地雷達探測 |
| `/instances/` | 工程實績 |
| `/contact/` | 聯繫我們 |