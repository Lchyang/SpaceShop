import requests
import json
import time
from django.conf import settings
from celery import shared_task
from celery import Task
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response


class CallbackTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('success task_id:{}'.format(task_id))
        return redirect('/users/code/')

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('failure')


class YunPianSms(object):
    """
    云片网发送信息.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, mobile, text):
        """ 发送验证码信息.
        """
        params = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': text
        }
        time.sleep(5)
        response = requests.post(self.url, data=params)
        return json.loads(response.text)


@shared_task(base=CallbackTask)
def add(x, y):
    return x + y


@shared_task(base=CallbackTask)
def send_sms_task(mobile, text):
    yun_pian = YunPianSms(api_key=settings.YUNPIAN_APIKEY)
    result = yun_pian.send_sms(mobile, text)
    return result


if __name__ == "__main__":
    from SpaceShop.settings import YUNPIAN_APIKEY

    send_sms = YunPianSms(YUNPIAN_APIKEY)
    res = send_sms.send_sms("18831627116", "【李春杨】您的验证码是1234。如非本人操作，请忽略本短信")
    print(res)
