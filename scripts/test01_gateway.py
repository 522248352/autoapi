import pytest

from api.api_gateway import ApiGateway
from tools.get_sale_data import getSaleData


class TestGateway(object):
    def setup_class(self):
        self.ob = ApiGateway()

    @pytest.mark.parametrize("casename,data", getSaleData())
    def test01_sale(self, casename, data):
        res = self.ob.api_sale(data=data)
        print(res.status_code)

if __name__ == "__main__":
    pytest.main(["-v","test01_gateway.py"])