# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo

class CompanyspiderPipeline(object):
    def process_item(self, item, spider):
        return item
'''执行数据库表的操作'''
class MysqlPipeline(object):
    def __init__(self,host,user,password,database,port):
        self.host = host
        self.user = user
        self.database = host
        self.password = password
        self.port = host

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host = crawler.settings.get("MYSQL_HOST"),
            user = crawler.settings.get("MYSQL_USER"),
            password = crawler.settings.get("MYSQL_PASS"),
            database = crawler.settings.get("MYSQL_DATABASE"),
            port = crawler.settings.get("MYSQL_PORT")
        )
    '''打开数据库连接'''
    def open_spider(self,spider):
        print(self.host)
        print(self.user)
        print(self.password)
        print(self.database)
        print(self.port)
        self.db = pymysql.connect(self.host,self.user,self.password,"test",charset="utf8",port=3306)
        self.Cursor = self.db.cursor()
    # 操作数据库
    def process_item(self, item, spider):
        sql = "insert into companybj(url,CompanyName,mode,location,contentHtml) values('%s','%s','%s','%s','%s')"%(item['url'],item['CompanyName'],item['mode'],item['location'],"")
        self.Cursor.execute(sql)
        self.db.commit()
        return item
    # 关闭数据库
    def close_spider(self,spider):
        self.db.close()


class MongoPipeline(object):
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        database = self.client[spider.name]
        data = dict(item)
        _id = database["Data"].insert(data)
        print(_id)
