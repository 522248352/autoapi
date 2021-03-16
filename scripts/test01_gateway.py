import pytest

from api.api_gateway import ApiGateway
from tools.get_log import GetLog
from tools.get_sale_data import getSaleData
from tools.tool import Tool

logger = GetLog.get_logger()


class TestGateway(object):
    def setup_class(self):
        self.ob = ApiGateway()
        logger.info(f"执行 set up")

    @pytest.mark.parametrize("casename,data", getSaleData())
    def test01_sale(self, casename, data):
        logger.info(f"开始执行{casename}-SALE接口请求")
        res = self.ob.api_sale(data=data)
        logger.info(f"结束执行{casename}-SALE接口请求，返回响应结果是：=={res.text}")
        Tool.sale_assert(res, data)



if __name__ == "__main__":
    pytest.main(["-v", "test01_gateway.py"])
