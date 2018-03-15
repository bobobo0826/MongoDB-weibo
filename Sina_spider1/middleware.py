# encoding=utf-8
import random
from Sina_spider1.cookies import cookies
from Sina_spider1.user_agents import agents


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ 换Cookie """

    def process_request(self, request, spider):
        cookie = random.choice(cookies)
        cookie = eval(cookie)  # 将str类型的cookie转换成dict
        request.cookies = cookie
