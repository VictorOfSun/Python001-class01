# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pymysql
from .items import PhoneItem, CommentItem

dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'test'
}


class ConnDB(object):
    def __init__(self, dbInfo, sql):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sql = sql

    def run(self, data):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        # 异常处理
        try:
            cur.execute(self.sql, data)
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

    def select(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        # 异常处理
        try:
            res = cur.execute(self.sql)
            # 关闭游标
            cur.close()
            conn.commit()
            if res is None:
                return 'no repeat'
            else:
                return 'repeat'
        except:
            conn.rollback()
            return
        # 关闭数据库连接
        conn.close()


class SpidersPipeline:
    def process_item(self, item, spider):

        # 把dict转换成dataframe，要先转成list
        # soda = [item]
        #
        # soda1 = pd.DataFrame(data=[item])
        # mode='a'是代表追加数据，不覆盖
        # soda1.to_csv('./movie1.csv', encoding='utf8', index=False, mode='a', header=False)

        res = ""

        # 判断当下插入的是手机/评论
        if isinstance(item, PhoneItem):
            sql = "insert into phone(name,time) values (%s,%s)"
            data = (item['name'], item['time'])
        else:
            sql = "insert into phone_co(name,time,comment) values (%s,%s,%s)"
            data = (item['name'], item['time'], item['comment'])

            # 判断该条记录是否已被插入
            select_db = ConnDB(dbInfo, "select * from phone where comment = '%s' " % item['comment'])
            res = select_db.select()

        # 如果记录已被插入过，则不再插入
        if res != 'repeat':
            db = ConnDB(dbInfo, sql)
            # 插入数据库-异常处理
            try:
                db.run(data)
            except Exception as e:
                print(e)

        return item

