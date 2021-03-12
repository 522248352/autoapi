import time
from random import random, randint


def saledata(comm,sale):
    """
    请求参数 处理逻辑
    :return: 返回 符合 pytest.mark.parametrize 的类型 [(),(),()]
    """

    # 获取公共请求参数 字典类型
    commonData = read_yaml.get_yamlDataOne(comm)

    # 获取 商户信息、特定请求参数（卡号、商户号、URL等）
    saleDatas = read_yaml.get_yamlDataTwo(sale)

    casename1 = []
    # heads1 = []
    # params1 = []
    others = []
    urls = []
    mark1 = []
    for i in saleDatas:

        i["others"]["data"].update(commonData)

        # 获取时间戳，生成transactionID
        t = time.time()
        # i["params"]["transactionId"] = str(int(round(t * 1000)))[0:8]
        i["others"]["data"]["transactionId"] = str(randint(0, 99999999)).zfill(8)


        # 组合待加签的数据
        waitencrypt = i["others"]["data"]["merchantNo"] + i["others"]["data"]["subAccount"] + \
                      i["others"]["data"]["transactionId"] + commonData["currency"] + \
                      i["others"]["data"]["amount"] + commonData["firstName"] + \
                      commonData["lastName"] + i["others"]["data"]["cardNumber"] + \
                      commonData["year"] + commonData["month"] + commonData["cvv"] + \
                      commonData["email"] + i["keys"]

        sign = data_encrypt.dataEncrypt(waitencrypt)
        logger.info("%s的签名sign是===%s"%(i["casenames"],sign))
        i["others"]["data"]["sign"] = sign

        casename1.append(i["casenames"])
        # heads1.append(i["heads"])
        # params1.append(i["params"])
        others.append(i['others'])
        urls.append(i['urls'])
        
        marklist = i['mark']
        for x,y in enumerate(marklist):
            marklist[x] = dic1[y]
        mark1.append(marklist)
        
    das = list(zip(casename1,urls,others,mark1))

    #转换成 pytest.param（）
    datasMark = addMark(das)
    return datasMark

if __name__ == '__main__':
    s = newsale("commondata_sale.yml", "sale.yml")
    print(s)