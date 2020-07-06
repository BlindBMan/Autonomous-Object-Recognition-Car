from ..items import ImagespiderItem
import scrapy
import json


class ImageSpider(scrapy.Spider):
    name = 'image_spider'
    # change for images with perfume bottles
    base_url = 'https://unsplash.com/napi/search/photos?query=perfume%20bottle&xp=&per_page=20&page='
    # base_url = 'https://unsplash.com/napi/search/photos?query=cup&xp=&per_page=20&page='
    start_urls = [base_url + '1']
    max_pages = 15
    curr_page = 1

    def parse(self, response):
        data = json.loads(response.body)
        inner_json = data.get('results')
        for jS in inner_json:
            url = jS.get('urls').get('small') + '.jpeg'
            yield ImagespiderItem(image_urls=[url])

        if self.curr_page <= self.max_pages:
            self.curr_page += 1
            yield scrapy.Request(self.base_url + f'{self.curr_page}')
