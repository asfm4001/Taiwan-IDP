# Framework
```python
.
├── README.md
├── requirements.txt
├── manage.py
├── db.sqlite3
├── dockerfile
├── core
│   ├── __init__.py
│   ├── asgi.py         # 非同步部署入口
│   ├── jinja2_env.py   # jinja2設定檔
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quotations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── autoNum.py
│   ├── migrations/
│   ├── models.py
│   ├── static/
│   ├── templates
│   ├── tests/
│   ├── urls.py
│   └── views.py
├── pages
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── static/
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── staticfiles/
└── templates/
```

# 套件
* Django==5.1.7
* gunicorn==23.0.0
* whitenoise==6.11.0

# Logs
### 20260512
* 將Google Cloud Run轉址至[https://taiwan-idp.com/](taiwan-idp.com/)，保留原Cloud Run網址