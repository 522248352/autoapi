import api
import requests

from tools.get_log import GetLog

logger = GetLog.get_logger()


class ApiGateway(object):
    def __init__(self):
        self.url_sale = api.host_gateway + "/gateway/TPInterface"
        self.url_checkout = api.host_gateway + "/gateway/Interface"

    def api_sale(self, data):
        logger.info(f"sale接口请求url=={self.url_sale}")
        logger.info(f"sale接口请求headers参数=={api.headers}")
        logger.info(f"sale接口请求参数=={data}")
        return requests.post(url=self.url_sale, headers=api.headers, data=data)

    def api_checkout(self, data):
        return requests.post(url=self.url_checkout, headers=api.headers, data=data)
