from .base import *

SECRET_KEY = os.environ['SPACE_SHOP_SECRET_KEY']
DB_PASSWORD = os.environ['SPACE_SHOP_DB_PASSWORD']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'space_shop',
        'HOST': '81.70.37.90',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': DB_PASSWORD
    }
}

YUNPIAN_APIKEY = os.environ['SPACE_SHOP_YUNPIAN_APIKEY']
YUNPIAN_TEXT = "【李春杨】您的验证码是{}。如非本人操作，请忽略本短信"

