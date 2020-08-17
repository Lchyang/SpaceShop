import requests
import json


class YunPianSms(object):
    """
    云片网发送信息.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, mobile, text):
        """ 发送验证码信息.
        :param mobile: str
        :param text: str
        :return: str
        """
        params = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': text
        }
        response = requests.post(self.url, data=params)
        return json.loads(response.text)


if __name__ == "__main__":
    from SpaceShop.settings import YUNPIAN_APIKEY

    send_sms = YunPianSms(YUNPIAN_APIKEY)
    res = send_sms.send_sms("18831627116", "【李春杨】您的验证码是1234。如非本人操作，请忽略本短信")
    print(res)
