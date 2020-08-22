from .base import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DB_PASSWORD = os.environ['DJANGO_DB_PASSWORD ']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'space_shop',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': DB_PASSWORD
    }
}

YUNPIAN_APIKEY = os.environ['YUNPIAN_APIKEY']
YUNPIAN_TEXT = "【李春杨】您的验证码是{}。如非本人操作，请忽略本短信"

