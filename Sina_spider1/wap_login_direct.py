import base64
import json
from urllib.parse import quote_plus
import requests
import time

session = requests.session()

headers = {
    'Host': 'passport.weibo.cn',
    'Origin': 'https://passport.weibo.cn',
    'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn&',
    'User-Agent':  'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 ',
 }


def wap_login(username,password):

    loginURL = 'https://passport.weibo.cn/sso/login'
    post_data = {
        'username': username,
        'password': password,
        'savestate': '1',
        'r': 'http://weibo.cn',
        'ec': '0',
        'entry': 'mweibo',
    }

    response = session.post(loginURL,data=post_data,headers=headers)
    if response.status_code != 200:
        raise Exception('模拟登陆失败')
    else:
        print("模拟登陆成功")


        return json.dumps(session.cookies.get_dict())


#测试专用
# if __name__=='__main__':
#
#     username = '17084633974'
#     password = 'haha123456'
#     wap_login(username,password)



