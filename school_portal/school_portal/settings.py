from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import os

# تحميل المتغيرات من .env
load_dotenv()

# مسار المشروع الأساسي
# مسار المشروع الأساسي
BASE_DIR = Path(__file__).resolve().parent.parent
print(f"DEBUG: BASE_DIR is {BASE_DIR}")
print(f"DEBUG: Frontend dist path is {(BASE_DIR.parent / 'frontend' / 'dist').resolve()}")
print(f"DEBUG: Frontend index exists? {(BASE_DIR.parent / 'frontend' / 'dist' / 'index.html').exists()}")

# الأمان
    # os.getenv("DEBUG", "False") == "True"
DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')

if not SECRET_KEY:
    raise ValueError("The SECRET_KEY setting must not be empty!")

ALLOWED_HOSTS = ['*']
#     "ta3lemi-fi-yadi.onrender.com",     "www.ta3lemi-fi-yadi.onrender.com",

# HTTPS & Security
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
CSRF_TRUSTED_ORIGINS = ["https://ta3lemi-fi-yadi.onrender.com", "http://localhost:5173", "http://127.0.0.1:5173"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'rest_framework',
    # تطبيقات المشروع
    'core',
    'academics',
    'attendance',
    'transfers',
    'assignments',
    'competitions',
    'ai_chat',
    'audit',
    'rest_framework',
    'corsheaders',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'school_portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            (BASE_DIR.parent / 'frontend' / 'dist').resolve(),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'school_portal.wsgi.application'

# قاعدة البيانات
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'), conn_max_age=600, ssl_require=True)
}

# Validators لكلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# إعدادات اللغة والتوقيت
LOGIN_REDIRECT_URL = '/core/'
LOGOUT_REDIRECT_URL = '/core/'
LOGIN_URL = '/core/login/'

# بريد إلكتروني SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS')
DEFAULT_FROM_EMAIL = f"تعلمي في يدي <{os.getenv('EMAIL_USER')}>"

# Cohere API Key
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# ملفات static و media
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    (BASE_DIR.parent / 'frontend' / 'dist' ).resolve(),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Cache Storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
