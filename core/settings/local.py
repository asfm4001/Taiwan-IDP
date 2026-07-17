from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CSRF 信任來源
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
]

# HTTPS 設定
SECURE_PROXY_SSL_HEADER = ("X-Forwarded-Proto", "https")
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SAMESITE = "Lax"

# SMTP Configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  #SMTP伺服器
# EMAIL_PORT = 587  #TLS通訊埠號
# EMAIL_USE_TLS = True  #開啟TLS(傳輸層安全性)
# EMAIL_HOST_USER = os.getenv("EMAIL")  #寄件者電子郵件
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")  #Gmail應用程式的密碼(含空格)