# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from wx_bitcoin.items import WxBitcoinItem
from scrapy.http.request import Request


class WxBtcSpider(scrapy.Spider):
    name = 'wx_btc'
    allowed_domains = ['sogou.com']
    start_urls = [
        'http://weixin.sogou.com/weixin?type=2&s_from=input&query=btc&ie=utf8&_sug_=n&_sug_type_=',
        # 'http://weixin.sogou.com/weixin?type=2&s_from=input&query=eth&ie=utf8&_sug_=n&_sug_type_=',
        # 'http://weixin.sogou.com/weixin?type=2&s_from=input&query=eos&ie=utf8&_sug_=n&_sug_type_='
    ]
    host_url = "http://weixin.sogou.com/weixin"

    def parse(self, response):
        self.logger.info('正在抓取的链接为：{}'.format(response.url))
        data_list = response.xpath('//ul[@class="news-list"]/li')
        print(data_list)
        if data_list:
            for each_data in data_list:
                wx_item = ItemLoader(item=WxBitcoinItem(), selector=each_data)
                wx_item.add_xpath('title', 'div[@class="txt-box"]/h3/a')
                wx_item.add_xpath('link', 'div[@class="txt-box"]/h3/a/@href')
                wx_item.add_xpath('author', 'div[@class="txt-box"]/div/a/text()')
                yield wx_item.load_item()

            # 下一页,未登录获取前10页数据
            next_page = response.xpath('//a[@id="sogou_next"]/@href')
            if next_page:
                next_page_url = self.host_url + next_page.extrat_first()
                yield Request(next_page_url, callback=self.parse)
        else:
            self.logger.error('xpath parser is wrong, please check it.')