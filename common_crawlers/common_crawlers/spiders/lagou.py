# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from common_crawlers.items import LaGouItemLoader, LaGouJobItem
from common_crawlers.utils.common import get_number, now_time


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'zhaopin/.*?'), follow=True),
        # Rule(LinkExtractor(allow=r'gongsi/\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=True),
    )

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://www.lagou.com/',
            'host': 'www.lagou.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.181 Safari/537.36'
        }
    }

    def parse_item(self, response):
        self.logger.info('>>>>>>正在抓取的url是：{}'.format(response.url))
        loader = LaGouItemLoader(item=LaGouJobItem(), response=response)
        loader.add_value('job_url', response.url)
        loader.add_value('job_url_id', get_number(response.url))
        loader.add_xpath('job_title', '//div[@class="job-name"]/@title')
        loader.add_xpath('min_job_salary', '//dd[@class="job_request"]/p/span[1]/text()')
        # loader.add_css('min_job_salary', '.job_request > p > span::text')
        loader.add_xpath('max_job_salary', '//dd[@class="job_request"]/p/span[1]/text()')
        loader.add_xpath('job_city', '//dd[@class="job_request"]/p/span[2]/text()')
        loader.add_xpath('job_work_years', '//dd[@class="job_request"]/p/span[3]/text()')
        loader.add_xpath('job_degree_need', '//dd[@class="job_request"]/p/span[4]/text()')
        loader.add_xpath('job_type', '//dd[@class="job_request"]/p/span[5]/text()')
        loader.add_xpath('job_publish_time', '//p[@class="publish_time"]/text()')
        loader.add_xpath('job_tags', '//ul[@class="position-label clearfix"]/li/text()')
        loader.add_xpath('job_advantage', '//dd[@class="job-advantage"]/p/text()')
        loader.add_xpath('job_desc', '//dd[@class="job_bt"]/div/p/text()')
        loader.add_xpath('job_addr', '//div[@class="work_addr"]')
        loader.add_xpath('job_comp_url', '//ul[@class="c_feature"]/li/a/@href')
        loader.add_xpath('job_comp_name', '//h2[@class="fl"]/text()')
        loader.add_value('crawl_time', now_time())
        loader.add_value('crawl_update_time', now_time())
        return loader.load_item()
