import scrapy
#Selenium 미들웨어 읽어들이기
from ..selenium_middleware import *

#쿠팡 이메일과 비밀번호 지정
USER = "ddd"
PASSWORD = "aaaaaa"


class CoupangSpider(scrapy.Spider):
    name = 'coupang1'
    #미들웨어 등록
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "coupang.selenium_middleware.SeleniumMiddleware": 0
        }
    }
    
    #요청 전에 로그인
    def start_requests(self):
        #로그인 페이지로 이동 후 로그인
        selenium_get("https://login.coupang.com/login/login.pang")
        email = get_dom('._loginForm [name=email]')
        email.send_keys(USER)
        password = get_dom('._loginForm [name=password]')
        password.send_keys(PASSWORD)
        button = get_dom("._loginForm button[type=submit]")
        button.click()
        
        #마이페이지로 이동
        a = get_dom('#myCoupang > a')
        mypage = a.get_attribute('href')
        yield scrapy.Request(mypage, self.parse)
        
    def parse(self, response):
        #원하는 정보 추출
        items = response.css('.my-order-unit__item-info')
        for item in items:
            title = item.css(".my-order-unit__info-name strong:last-child::text").extract_first().strip()
            info = item.css(".my-order-unit__info-ea::text").extract_first().split("/")[0].strip()
            yield {
                "title": title,
                "info" : info
            }
        


    def parse(self, response):
        pass
