import pymysql

lista=list()
#封装一个模块，操作数据库
class MYSQLdbUtil():
    def __init__(self,host='localhost',name='root',pwd='123456',port='3306',dbname='test',charset='utf8'):
        self.__host=host
        self.__name=name
        self.__pwd=pwd
        self.__port=port
        self.__dbname=dbname
        self.__charset=charset
        self.__connection=None
        self.__cursor=None

    def getConnection(self):
        try:
            self.__connection=pymysql.connect(self.__host,self.__name,self.__pwd,self.__dbname,charset=self.__charset)
        except (pymysql.MySQLError,pymysql.DatabaseError):
            pass
        pass


    #DML操作
    def execute(self,sql,params=None,isbatch=False):
        try:
            self.getConnection()
            self.__cursor=self.__connection.cursor()
            if params:
                if isbatch:
                    return self.__cursor.execute(sql,params)
                else:
                    return self.__cursor.execute(sql)
            else:
                return self
                pass
        except:
            self.__cursor.close()
            self.__connection.close()
        pass

    # 查询操作
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.__cursor.fetchall()
        pass

    #关闭方法，为了支持事物

    def close(self):
        if self.__cursor and self.__connection:
            self.__cursor.close()
            self.__connection.close()

    #提交
    def commit(self):
        self.__connection.commit()
        pass
    #回滚
    def rollback(self):
        self.__connection.rollback()


if __name__=='__main__':
    pass
    '''
    dbu=MYSQLdbUtil()
    dbu.getConnection()  #开启事物

    try:
        sql = "insert into jobs (职位名,公司名,工作地点,薪资,发布时间)values('python开发师','上海交大','北京海淀区','15k-20k','8-29')"
        #datalist = [(30001, 'allpa30001', '123456'),(30002, 'allpa30002', '123456'),(30003, 'allpa30003', '123456')]
        dbu.execute(sql, True)
        dbu.commit()
    except:
        #syslogger.logger.error("执行SQL：" + sqlinsert + " 出现异常回滚。")
        print('失败')
        dbu.rollback()
        dbu.commit()  # 回滚后要提交
    finally:
        dbu.close()

    
    #更新数据
    try:
        sql1="update t_info set eat=%s where name=%s "
        dbu.execute(sql1,('蔬菜','guajie'))
        dbu.commit()
    except:
        dbu.rollback()
        dbu.commit()  #回滚后要提交
    finally:
        dbu.close()
    '''

    '''
    # 删除数据
    try:
        sql2 = "delete from t_info where id=%s"
        dbu.execute(sql2, (13))
        dbu.commit()
    except:
        dbu.rollback()
        dbu.commit()  # 回滚后要提交
    finally:
        dbu.close()
    '''