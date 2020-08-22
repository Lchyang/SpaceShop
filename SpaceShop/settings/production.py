from .base import *

# SECRET_KEY = os.environ['SPACE_SHOP_SECRET_KEY']
# DB_PASSWORD = os.environ['SPACE_SHOP_DB_PASSWORD']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'space_shop',
        'HOST': '81.70.37.90',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456'
    }
}

SECRET_KEY = 'g5q!dsx7wh^cv)40_lix&k5u3p7=bq0r#)-oq7ytxk@_3l8-uk'

YUNPIAN_APIKEY = "756f2d59ff694f7f8ea3ea027dd9492c"
# YUNPIAN_APIKEY = os.environ['SPACE_SHOP_YUNPIAN_APIKEY']
YUNPIAN_TEXT = "【李春杨】您的验证码是{}。如非本人操作，请忽略本短信"

