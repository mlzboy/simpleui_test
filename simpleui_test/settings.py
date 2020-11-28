"""
Django settings for simpleui_test project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CODEMIRROR_PATH = r"static-5.58.2"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%d+))3*j8)8w1vqd9-l-hg^+(&0_wxf=x&e6d2jeu72jj%)b0u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simditor',
    'django_extensions',
    'oj',
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',

    # 'captcha'
]


SIMDITOR_TOOLBAR = [
    'title', 'bold', 'italic', 'underline', 'strikethrough', 'fontScale',
    'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|', 'link',
    'image', 'hr', '|', 'indent', 'outdent', 'alignment', 'fullscreen',
    'markdown', 'emoji'
]

SIMDITOR_CONFIGS = {
    'toolbar': SIMDITOR_TOOLBAR,
    'upload': {
        'url': '/simditor/upload/',
        'fileKey': 'upload'
    },
    'emoji': {
        'imagePath': '/static/simditor/images/emoji/'
    }
}
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


SIMDITOR_UPLOAD_PATH = 'uploads/'
SIMDITOR_IMAGE_BACKEND = 'pillow'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'simpleui_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'simpleui_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'simpleui_test',  # 数据库名
        'USER': 'root',  # 数据库账户名
        'PASSWORD': 'zhoubt',  # 即user_password，数据库密码。
        # 为安全起见，应从系统环境变量中获取。os.environ['MY_DB_PASS']
        # 'HOST': '127.0.0.1',  # 数据库服务器IP
        'HOST': '106.75.10.125',  # 数据库服务器IP
        'PORT': '3333',  # 端口
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATIC_URL = '/static/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
print("="*20)
print(STATIC_ROOT)
print(BASE_DIR)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 自定义simpleui 菜单
# SIMPLEUI_CONFIG = {
#     # 在自定义菜单的基础上保留系统模块
#     'system_keep': True,
#     'menus': [{
#         'name': 'Simpleui',
#         'icon': 'fas fa-code',
#         'url': 'https://gitee.com/tompeppa/simpleui'
#     }, {
#         'app': 'auth',
#         'name': '权限认证',
#         'icon': 'fas fa-user-shield',
#         'models': [{
#             'name': '用户',
#             'icon': 'fa fa-user',
#             'url': 'auth/user/'
#         }]
#     }, {
#         'name': '测试',
#         'icon': 'fa fa-file',
#         'models': [{
#             'name': 'Baidu',
#             'url': 'http://baidu.com',
#             'icon': 'far fa-surprise'
#         }, {
#             'name': '内网穿透',
#             'url': 'https://www.wezoz.com',
#             'icon': 'fab fa-github'
#         }, {
#             'name': '内网穿透',
#             'url': 'https://www.wezoz.com',
#             'icon': 'fab fa-github'
#         }, {
#             'name': '登录页嵌套测试',
#             'url': '/login'
#         }]
#     }]
# }

SIMPLEUI_HOME_INFO = False

