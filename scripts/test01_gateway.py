import pytest

from api.api_gateway import ApiGateway
from tools.get_log import GetLog
from tools.get_sale_data import getSaleData

logger = GetLog.get_logger()


class TestGateway(object):
    def setup_class(self):
        self.ob = ApiGateway()

    @pytest.mark.parametrize("casename,data", getSaleData())
    def test01_sale(self, casename, data):
        logger.info(f"开始执行{casename}-SALE接口请求")
        res = self.ob.api_sale(data=data)
        logger.info(f"结素执行{casename}-SALE接口请求")
        print(res.text)


if __name__ == "__main__":
    pytest.main(["-v", "test01_gateway.py"])
