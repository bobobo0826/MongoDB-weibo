# MongoDB-weibo
爬取微博内容，保存数据到MongoDB

1.在cookies.py中填入微博用户名和密码

2.根据用户名和密码选择合适的登录方式
  选择的账号不出现验证码：设置COOKIE_GETWAY=2
  选择的账号出现验证码：设置COOKIE_GETWAY=1
  
3.选择爬取的微博账号的id

4.运行时在终端输入：scrapy crawl sinaSpider
