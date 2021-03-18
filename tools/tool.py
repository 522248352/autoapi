import re

from tools.get_log import GetLog
from tools.oracle_db import Read_db

logger = GetLog.get_logger()


class Tool(object):

    @classmethod
    def sale_assert(cls, response, data):
        # 获取返回结果中的数据
        logger.info("开始执行断言方法。。。")
        try:
            transactionId = re.search("<transactionId>(.*?)</transactionId>", response.text).group(1)
            tradeNo = re.search("<tradeNo>(.*?)</tradeNo>", response.text).group(1)
            orderInfo = re.search("<orderInfo>(.*?)</orderInfo>", response.text).group(1)
        except Exception as e:
            logger.error('==正则获取 transactionId值  或者 tradeNo值 或者 orderInfo值 错误！！！')
            raise
        logger.info(f"正则获取的：transactionId值===={transactionId},"
                    f"tradeNo值===={tradeNo}, "
                    f"orderInfo值===={orderInfo}")

        # 断言响应结果返回

        logger.info(f"断言响应结果返回：实际orderInfo===={orderInfo}：：预期是：0000:Success")
        logger.info(f"响应结果状态断言：实际是{response.status_code}::预期是 200")
        logger.info(f"响应结果数据断言：实际是transactionId={transactionId}::预期是 {data.get('transactionId')}")
        try:
            assert orderInfo == "0000:Success"
            assert 200 == response.status_code
            assert transactionId == data.get('transactionId')
        except AssertionError as e:
            logger.error(f"断言有问题咯、、、{e}")
            raise

    @classmethod
    def sale_db_assert(cls, response, data):

        try:
            tradeNo = re.search("<tradeNo>(.*?)</tradeNo>", response.text).group(1)
        except Exception as e:
            logger.error(f"通过正则获取订单流水号有误。。。{e}")
            raise
        sql1 = f"SELECT TR_CURRENCY,TR_AMOUNT,TR_STATUS,TR_PAYMENT_STATUS," \
               f"TR_BANKCURRENCY,TR_BANKAMOUT,TR_BANK_CODE,TR_BANKRETURNCODE," \
               f"TR_BANKINFO,TR_NOTIFYURL,TR_CAPTURED,TR_CAPTURE_TIME,TR_INF_TYPE," \
               f"TR_CARDTYPE " \
               f"FROM CCPS_TRADERECORD WHERE TR_NO = '{tradeNo}'"

        sql2 = f"SELECT * FROM CCPS_TRADERECORD_STATUS where TR_NO ='{tradeNo}'"
        db = Read_db()
        resu1 = db.get_sql_data(sql1)
        resu2 = db.get_sql_data(sql2)
        try:
            logger.info(f"CCPS_TRADERECORD断言：实际查询结果条数===={len(resu1)}：：预期是：1")
            logger.info(f"CCPS_TRADERECORD断言：实际查询币种是===={resu1[0][0]}：：预期是：{data.get('currency')}")
            logger.info(f"CCPS_TRADERECORD断言：实际查询状态是===={resu1[0][2]}：：预期是：1")
            assert len(resu1) == 1
            assert resu1[0][0] == data.get('currency')
            assert resu1[0][2] == 1
        except AssertionError as e:
            logger.error(f"数据库断言异常、、、{e}")
            raise
