# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonMobilesItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?i=electronics&bbn=1805560031&rh=n%3A976419031%2Cn%3A976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031&page=2',]
    page_num=3
    def parse(self, response):
        items=AmazonMobilesItem()
        mobile_name=response.css('.a-color-base.a-text-normal::text').extract()
        mobile_price=response.css('.a-price-whole::text').extract()
        mobile_image=response.css('.s-image::attr(src)').extract()
        items['mobile_name']=mobile_name
        items['mobile_price']=mobile_price
        items['mobile_image']=mobile_image
        yield items
        next_page='https://www.amazon.in/s?i=electronics&bbn=1805560031&rh=n%3A976419031%2Cn%3A976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031&page='+str(AmazonSpiderSpider.page_num)
        if AmazonSpiderSpider.page_num<4:
        	AmazonSpiderSpider.page_num+=1
        	yield response.follow(next_page,callback=self.parse)
