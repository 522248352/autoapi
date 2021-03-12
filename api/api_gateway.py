import api
import requests


class ApiGateway(object):
    def __init__(self):
        self.url_sale = api.host_gateway + "/gateway/TPInterface"
        self.url_checkout = api.host_gateway + "/gateway/Interface"

    def api_sale(self, data):
        return requests.post(url=self.url_sale, headers=api.headers, data=data)

    def api_checkout(self, data):
        return requests.post(url=self.url_checkout, headers=api.headers, data=data)