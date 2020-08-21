from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'space_shop',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456'
    }
}

YUNPIAN_APIKEY = "756f2d59ff694f7f8ea3ea027dd9492c"
YUNPIAN_TEXT = "【李春杨】您的验证码是{}。如非本人操作，请忽略本短信"

SECRET_KEY = 'g5q!dsx7wh^cv)40_lix&k5u3p7=bq0r#)-oq7ytxk@_3l8-uk'
