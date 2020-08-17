import xadmin
from .models import VerifyCode


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "modified_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
