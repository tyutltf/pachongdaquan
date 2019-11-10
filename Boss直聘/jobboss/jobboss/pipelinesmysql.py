# -*- coding: utf-8 -*-
from week5_day04.dbutil import dbutil

# 作业： 自定义的管道，将完整的爬取数据，保存到MySql数据库中
class JobspidersPipeline(object):
    def process_item(self, item, spider):
        dbu = dbutil.MYSQLdbUtil()
        dbu.getConnection()  # 开启事物

        # 1.添加
        try:
            sql = "insert into boss_job (job_title,compensation,company,address,seniority,education,company_type,company_finance,company_quorum)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            #date = []
            #dbu.execute(sql, date, True)
            dbu.execute(sql, (item["job_title"],item["compensation"],item["company"],item["address"],item["seniority"],item["education"],item["company_type"],item["company_finance"],item["company_quorum"]),True)
            dbu.commit()
            print('插入数据库成功！！')
        except:
            dbu.rollback()
            dbu.commit()  # 回滚后要提交
        finally:
            dbu.close()
        return item