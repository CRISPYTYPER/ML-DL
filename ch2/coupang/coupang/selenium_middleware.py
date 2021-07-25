from scrapy.http import HtmlResponse
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#파이어폭스 초기화
driver = Firefox()

#파이어폭스로 URL 열기
def selenium_get(url):
    driver.get(url)
    
#CSS 쿼리를 지정해서 읽어 들일 때 까지 대기
def get_dom(query):
    dom = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,query)))
    return dom

#파이어폭스 종료
def selenium_close():
    driver.close()
    
#미들웨어
class SeleniumMiddleware(object):
    #요청을 Selenium으로 처리
    def process_request(self,request,spider):
        driver.get(request.url)
        return HtmlResponse(
            driver.current_url,
            body = driver.page_source,
            encoding = 'utf-8',
            request = request)