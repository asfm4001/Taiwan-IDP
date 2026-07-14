# Project Structure 專案架構
```plaintext
quotations/
├── autoNum.py          # 報價單編號產生器
├── views.py            # 業務邏輯
├── urls.py             # URL 路由
├── models/             # 資料模型
├── templates/          # HTML 模板
├── static/             # 靜態資源
├── migrations/         # 資料庫遷移
└── tests/              # 測試程式
```

# URLs 路由
| 路由 (URL) | 頁面 |
|------------|------|
| `/quotations/preview/<int:pk>/` | 報價單預覽 |
| `/quotations/convert_to_order/<int:pk>` | 報價單轉訂單 |
| `/quotations/clone_from_worktype/<int:pk>` | 從工作類型複製報價單 |