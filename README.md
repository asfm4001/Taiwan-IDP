# Super admin
ID: superadmin
PW: xu3aj4fu0

# Framework
```python
.
├── README.md
├── compose.yaml
├── nginx/
└── django
    ├── .env                # 環境變數
    ├── db.sqlite3          # 資料庫
    ├── dockerfile
    ├── requirements.txt    # 套件
    ├── manage.py
    ├── hydraulicFirm
    │   ├── __init__.py
    │   ├── asgi.py         # 非同步部署入口
    │   ├── jinja2_env.py   # jinja2設定檔
    │   ├── settings.py     # 設定檔
    │   ├── urls.py         # 全域URL
    │   └── wsgi.py         # 部署入口
    ├── estimates
    │   ├── __init__.py
    │   ├── admin.py        # 後台設定檔
    │   ├── apps.py
    │   ├── migrations/     # 資料庫版控
    │   ├── models.py       # 資料庫模型
    │   ├── static/         # 靜態資源
    │   ├── templates/      # html模板
    │   ├── tests/          # 測試檔
    │   ├── urls.py         # app URL
    │   └── views.py        # app 邏輯
    ├── pages/              # app 2
    └── static/             # 全域靜態資源(部署用)
```

# 套件
* Django==5.1.7
* dotenv==0.9.9
* python-dotenv==1.1.0
* gunicorn==23.0.0
* Jinja2==3.1.6
* 