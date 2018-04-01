# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import codecs
import json
from scrapy.exporters import JsonItemExporter
from scrapy.conf import settings
from twisted.enterprise import adbapi
import MySQLdb
from scrapy.conf import settings


class CommonCrawlersPipeline(object):
    """默认的pipeline"""
    def process_item(self, item, spider):
        return item


class CustomJsonPipeline(object):
    """自定义存储结果到json文件中"""

    def __init__(self):
        super(CustomJsonPipeline, self).__init__()
        self.file = codecs.open('job_bole2.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def close_spider(self, spider):
        self.file.close()


class ExporterJsonPipeline(object):
    """调用JsonItemExporter存储结果到json文件中"""

    def __init__(self):
        self.file = open('job_bole2_with_exporter.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ThumbnailImagePipeline(ImagesPipeline):
    """保存缩略图的本地地址到item里"""
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_path = value.get('path', '')
            item['thumbnail_path'] = image_path
        return item


class MysqlPipeline(object):
    """自定义mysql存储items"""
    def __init__(self):
        params = dict(
            host=settings.get('MYSQL_HOST'),
            port=settings.get('MYSQL_PORT'),
            db=settings.get('MYSQL_DB'),
            user=settings.get('MYSQL_USER'),
            password=settings.get('MYSQL_PASSWORD'),
            charset='utf8'
        )
        self.conn = MySQLdb.connect(**params)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into crawler(title,thumbnail_url) values(%s,%s)"
        self.cursor.execute(sql, [item['title'], item['thumbnail_url']])
        self.conn.commit()
        return item

