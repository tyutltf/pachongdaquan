# -*- coding: utf-8 -*-
from week5_day04.dbutil import dbutil

# 作业： 自定义的管道，将完整的爬取数据，保存到MySql数据库中
class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        dbu = dbutil.MYSQLdbUtil()
        dbu.getConnection()  # 开启事物

        # 1.添加
        try:
            #sql = "insert into movies (电影排名,电影名称,电影短评,评价分数,评价人数)values(%s,%s,%s,%s,%s)"
            sql = "insert into t_movie (rank,moviename,movietips,grade,human)values(%s,%s,%s,%s,%s)"
            #date = [item['rank'],item['title'],item['quote'],item['star']]
            #dbu.execute(sql, date, True)
            dbu.execute(sql, (item['rank'],item['title'],item['quote'],item['star'][0],item['star'][1]),True)
            #dbu.execute(sql,True)
            dbu.commit()
            print('插入数据库成功！！')
        except:
            dbu.rollback()
            dbu.commit()  # 回滚后要提交
        finally:
            dbu.close()
        return item