import cx_Oracle
import tools
from tools.get_log import GetLog

logger = GetLog.get_logger()

# conn = cx_Oracle.connect("pay","he7qNGuS5Hu19Igz","192.168.200.247:1521/orcl")
# conn = cx_Oracle.connect("pay/he7qNGuS5Hu19Igz@192.168.200.247:1521/orcl")

class Read_db(object):
    # 创建连接对象
    conn = None

    # 获取连接对象
    def get_conn(self):
        if self.conn is None:
            self.conn = cx_Oracle.connect(tools.db["username"],tools.db["password"],tools.db["host_port_database"])
        # self.conn = cx_Oracle.connect("pay","he7qNGuS5Hu19Igz","192.168.200.247:1521/orcl")
        logger.info("======连接 success======")
        return self.conn

    # 获取游标对象
    def get_cursor(self):
        return self.get_conn().cursor()

    # 关闭游标对象
    def close_cursor(self, cursor):
        if cursor:
            cursor.close()

    # 关闭连接对象
    def close_conn(self):
        if self.conn:
            self.conn.close()
            # 关闭连接对象后，对象还存在内存中，需要手工设置为None
            self.conn = None

    # 获取查询结果集
    def get_sql_data(self, sql):
        # 定义游标对象及数据变量
        sursor = None
        data = None
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 调用执行方法
            sursor.execute(sql)
            # 获取结果
            data = sursor.fetchall()
        except Exception as e:
            print(f"查询sql异常，报错是{e}")
        finally:
            # 关闭游标对象
            self.close_cursor(sursor)
            # 关闭连接对象
            self.close_conn()
            # 返回结果
            return data

    # 更新结果集
    def update_sql_data(self, sql):
        # 定义游标对象及数据变量
        sursor = None
        data = None
        try:
            # 获取游标对象
            sursor = self.get_cursor()
            # 调用执行方法
            sursor.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print(f"更新sql异常，报错是{e}")
            # 回滚事务
            self.conn.rollback()
        finally:
            # 关闭游标对象
            self.close_cursor(sursor)
            # 关闭连接对象
            self.close_conn()


if __name__ == "__main__":

    db = Read_db()
    sql1 = "SELECT TR_CAPTURED,TR_BANKORDERNO,TR_CHECKED,TR_CHECKDATETIME,TR_STATUS,TR_IS_REPAY " \
           "FROM CCPS_TRADERECORD where TR_NO='3668430309045829632'"
    ss1 = db.get_sql_data(sql1)

    print(ss1)
    sql2 = "select TR_CURRENCY,TR_AMOUNT,TR_STATUS,TR_PAYMENT_STATUS,TR_BANKCURRENCY,TR_BANKAMOUT," \
           "TR_BANK_CODE,TR_BANKRETURNCODE,TR_BANKINFO,TR_NOTIFYURL,TR_CAPTURED,TR_CAPTURE_TIME,TR_INF_TYPE," \
           "TR_CARDTYPE from CCPS_TRADERECORD where tr_no ='3668430309045829632'"
    ss2 = db.get_sql_data(sql2)

    print(ss2)
    print(type(ss2))