from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = [
    "django-app-529979500146.asia-east1.run.app",   # for google cloud run
    "taiwan-idp.com",
    "www.taiwan-idp.com"
    ]   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRESQL_DB_NAME"),                # 資料庫名稱
        'USER': os.getenv("POSTGRESQL_DB_USER"),                # PostgreSQL 使用者
        'PASSWORD': os.getenv("POSTGRESQL_DB_PASSWORD"),
        'HOST': os.getenv("POSTGRESQL_DB_HOST"),                # DB server IP
        'PORT': os.getenv("POSTGRESQL_DB_PORT", '5432'),        # PostgreSQL 預設 port
    }
}

# CSRF 信任來源
CSRF_TRUSTED_ORIGINS = [
    "https://django-app-529979500146.asia-east1.run.app",   # for google cloud run
    "https://taiwan-idp.com",
    "https://www.taiwan-idp.com",
]

# HTTPS 設定
SECURE_PROXY_SSL_HEADER = ("X-Forwarded-Proto", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "Lax"