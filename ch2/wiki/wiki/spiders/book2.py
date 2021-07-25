import scrapy

class Book2Spider(scrapy.Spider):
    name = 'book2'
    start_urls = [
        'https://wikibook.co.kr/list/'
    ]
    
    def parse(self, response):
        #도서 목록 추출
        li_list = response.css('.book-url')
        for a in li_list:
            #href 속성과 텍스트 추출
            href = a.css('::attr(href)').extract_first()
            text = a.css('::text').extract_first()
            #절대 경로로 변환
            href2 = response.urljoin(href)
            #결과 내기
            yield {
                'text':text,
                'url':href2
            }