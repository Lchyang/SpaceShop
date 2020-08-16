import xadmin
from .models import VerifyCode, UserProfile


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "modified_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
