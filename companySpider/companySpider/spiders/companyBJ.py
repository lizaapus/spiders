# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import CompanyBJItem
import time

class CompanybjSpider(scrapy.Spider):
    name = 'companyBJ'
    allowed_domains = ['3618med.com']
    start_urls = ['http://www.3618med.com/company/a2-1.html']
    page = 1
    maxPage = 64

    def parse(self, response):
        divs = response.css('div.tia_qy_list')
        icount = 1 
        for div in divs:
            item = CompanyBJItem()
            item['ContentHtml'] = div.xpath("//div[@class='tia_qy_list']["+str(icount)+"]").extract_first()
            item['url'] = div.xpath(".//div[@class='tia_qy_pic1']//a/@href").extract_first()
            item['CompanyName'] = div.xpath(".//div[@class='tia_qy_pic1']//a/@title").extract_first()
            item['mode'] = div.re_first("<span>经营方式：(.*?)</span>")
            item['location'] = div.re_first("<span>所在地：(.*?)</span>")
            
            icount = icount+1
            # print(item)
            yield item
        
        self.page += 1
        if self.page <= self.maxPage:
            next_url = 'http://www.3618med.com/company/a2-'+str(self.page)+'.html'
            next_url =  response.urljoin(next_url)
            time.sleep(3)
            yield scrapy.Request(url=next_url,callback = self.parse)

