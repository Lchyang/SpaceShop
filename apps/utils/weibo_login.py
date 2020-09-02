def get_auth_url():
    base_url = 'https://api.weibo.com/oauth2/authorize'
    client_id = '2361548814'
    redirect_uri = 'http://81.70.37.90:8888/complete/weibo/'
    auth_url = base_url + '?client_id={}&redirect_uri={}'.format(client_id, redirect_uri)

    print(auth_url)
    # 'http://81.70.37.90:8888/complete/weibo/?code=f68d94f1d12d7e468161699f072be870'


def get_access_token():
    base_url = 'https://api.weibo.com/oauth2/access_token'
    import requests
    return_dict = requests.post(base_url, data={
        "client_id": "2361548814",
        "client_secret": "fe444d98d5457bad5ddab085c7f2f5e6",
        "grant_type": "authorization_code",
        "code": "221f4e78f1f43c7f3301be96d68c2a82",
        "redirect_uri": "http://81.70.37.90:8888/complete/weibo/"
    })
    return return_dict

def get_user_information(access_token, uid):
    base_url = 'https://api.weibo.com/2/users/show.json'




if __name__ == '__main__':
    # get_auth_url()
    get_access_token()
    # '{"access_token":"2.002tORsHAjooZCfc4a95b283CNqCcD","remind_in":"157679999","expires_in":157679999,"uid":"7214960791","isRealName":"true"}'
