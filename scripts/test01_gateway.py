import json
import re

import pytest

from api.api_gateway import ApiGateway
from tools.get_checkout_data import getCheckoutData
from tools.get_log import GetLog
from tools.get_sale_data import getSaleData
from tools.tool import Tool

logger = GetLog.get_logger()


class TestGateway(object):
    def setup_class(self):
        logger.info(f"set class 开始实例化api对象")
        self.ob = ApiGateway()

    @pytest.mark.parametrize("casename,data", getSaleData())
    def test01_sale(self, casename, data):
        logger.info(f"开始执行{casename}-SALE接口请求")
        res = self.ob.api_sale(data=data)
        logger.info(f"结束执行{casename}-SALE接口请求，返回响应结果是：=={res.text}")
        Tool.sale_assert(res, data)

    @pytest.mark.parametrize("casename,param_one,param_two", getCheckoutData())
    def test02_checkout(self, casename, param_one, param_two):

        logger.info(f"开始执行{casename}-CHECKOUT_NEW_SETUP接口请求")
        res_setup = self.ob.api_checkout_setup(data=param_one)
        logger.info(f"结束执行{casename}-CHECKOUT_NEW_SETUP接口请求，返回响应结果是：=={res_setup.text}")
        # 获取第一步操作后，重定向的URL链接
        re_url = res_setup.url
        logger.info(f"新收银台的url是：{re_url}")
        try:

            pathgetno = re.search(r".*?checkout/(.*)", re_url).group(1)
            logger.info(f"获取的pp ====={pathgetno}")
            trno = self.ob.api_get_trno(data=pathgetno)
        except Exception as e:
            logger.error(f"获取trno异常：{e}")
            raise
        param_two["tradeNo"] = trno
        res_down = self.ob.api_checkout_teardown(data=param_two)
        logger.info(res_down.status_code)

        # Tool.sale_assert(res, data)


if __name__ == "__main__":
    pytest.main(["-v", "test01_gateway.py"])
