from django.core.management.utils import get_random_secret_key
from pathlib import Path
import sys, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Location Apps
sys.path.append(
    os.path.join(BASE_DIR, "apps")
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-xetlkurkpaqsloru-ss-h$w&-%r#)2&heo=fob56^9bvm%xp#q)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xetlkurkpaqsloru-ss-h$w&-%r#)2&heo=fob56^9bvm%xp#q'

DEBUG = int(os.environ.get('DEBUG', 1))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '']

INTERNAL_IPS = ('*')

# Default Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Intern Apps
INSTALLED_APPS += [
    'core',
    'accounts',
    'tasks',
]

# Extern Apps
INSTALLED_APPS += [
    'bootstrap5',
    'compressor'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': str(os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3')),
        'NAME': str(os.environ.get('DB_NAME', BASE_DIR / 'db.sqlite3')),
        'USER': str(os.environ.get('DB_USER', '')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD', '')),
        'HOST': str(os.environ.get('DB_HOST', '')),
        'PORT': str(os.environ.get('DB_PORT', ''))
    }
}

if DEBUG:
    # COMPRESSOR CONFIG
    COMPRESS_DEBUG_TOGGLE = 'whatever'

    # DEBUG CONFIG
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: False if request.is_ajax() else True,
    }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

AUTH_USER_MODEL = "accounts.User"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#SMTP
EMAIL_BACKEND = str(os.environ.get('EMAIL_BACKEND', "django.core.mail.backends.console.EmailBackend"))
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = str(os.environ.get('EMAIL_HOST_USER', ""))
EMAIL_HOST_PASSWORD = str(os.environ.get('EMAIL_HOST_PASSWORD', ""))
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Tasks'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = False
COMPRESS_OFFLINE_MANIFEST = "manifest.json"
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter','compressor.filters.cssmin.CSSMinFilter']
COMPRESS_YUI_BINARY = os.path.join(BASE_DIR, 'bin/yui.sh')
COMPRESS_JS_FILTERS = ['compressor.filters.closure.ClosureCompilerFilter']
COMPRESS_CLOSURE_COMPILER_BINARY = os.path.join(BASE_DIR, 'bin/closure.sh')
COMPRESS_CLOSURE_COMPILER_ARGUMENTS = "--language_in=ECMASCRIPT5"