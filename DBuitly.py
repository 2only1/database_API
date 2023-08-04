import pymysql

class DBUtil:
    config = {
        'host':'localhost',
        'port':3306,
        'user':'root',
        'passwd': '123456',
        'db':'test',
        'charset':'utf8'
        }
    def __init__(self) -> None:

        '''
        获取连接
        获取游标
        '''
        self.con = pymysql.connect(**DBUtil.config) #以键值对的形式返回
        self.cursor = self.con.cursor()

    def close(self) -> None:
        print('执行关闭操作')
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()

    def execute_dml(self,sql,*args):
        '''
        执行DML语句,增删改查
        '''
        try:
            self.cursor.execute(sql,args)
            self.con.commit()
        except Exception as e:
            print(f'添加出现c错误=={e}')
            if self.con:
                self.con.rollback() #回滚
        finally:
            self.close()
    
    def query_fall(self,sql,*args):
        '''
        获取数据
        返回结果
        '''
        try:
            self.cursor.execute(sql,args)
            rs = self.cursor.fetchall()
            return rs
        except Exception as e:
            print(f'查询出现错误=={e}')
        finally:
            self.close()

if __name__ == '__main__':
    db = DBUtil()
    sql = 'show tables;'
    r = db.query_fall(sql)
    print(r)