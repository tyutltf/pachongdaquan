from 爬虫大全.dingdian.dingdian import dbutil

class LianjiaPipeline(object):
    def process_item(self, item, spider):
        dbu = dbutil.MYSQLdbUtil()
        dbu.getConnection()  # 开启事物

        # 1.添加
        try:
            #sql = "insert into movies (电影排名,电影名称,电影短评,评价分数,评价人数)values(%s,%s,%s,%s,%s)"
            sql = "insert into house (housename,houselurl,housedizhi,houseinfo,houseprice,houseperprice)values(%s,%s,%s,%s,%s,%s)"
            #date = [item['rank'],item['title'],item['quote'],item['star']]
            #dbu.execute(sql, date, True)
            dbu.execute(sql, (item['houseinfo'],item['houseurl'],item['housedizhi'],item['housexiangxi'],item['houseprice'],item['houseperprice']),True)
            #dbu.execute(sql,True)
            dbu.commit()
            print('插入数据库成功！！')
        except:
            dbu.rollback()
            dbu.commit()  # 回滚后要提交
        finally:
            dbu.close()
        return item