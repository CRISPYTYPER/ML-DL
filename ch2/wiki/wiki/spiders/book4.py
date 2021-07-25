import scrapy


class Book4Spider(scrapy.Spider):
    name = 'book4'
    allowed_domains = ['wikibook.co.kr']
    #도서 목록 페이지
    start_urls = [
        'https://wikibook.co.kr/list'
    ]
    
    #도서 목록 페이지 스크레이핑
    def parse(self, response):
        li_list = response.css('.book-url')
        for a in li_list[:5]:
            href = a.css('::attr(href)').extract_first()
            print(href)
            #개별 도서 페이지에 대한 크롤링 요청
            yield response.follow(
                response.urljoin(href),self.parse_book
            )
            
    #개별 도서 페이지를 스크레이핑 하는 함수
    def parse_book(self,response):
        title = response.url.split("/")[-2]
        img_url = response.css('.book-image-2d::attr(src)').extract_first()
        # 다운로드를 지시합니다.
        req = scrapy.Request(
            response.urljoin(img_url),
            callback=self.parse_img
        )
        #함수끼리 데이터를 전송하는 방법입니다.
        req.meta["title"]=title
        yield req
        
    #이미지 다운로드
    def parse_img(self, response):
        #전달된 데이터를 받습니다.
        title = response.meta["title"]
        title = title.replace(r'[\/:*?"<>|.]+','_').strip()
        fname = title+'.jpg'
        #파일을 저장합니다.
        with open(fname,'wb') as f:
            f.write(response.body)