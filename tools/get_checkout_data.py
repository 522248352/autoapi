import time
from random import randint
import tools
from tools import data_encrypt
from tools.data2pytest import dataToPytest
from tools.read_yaml import read_yaml


def getCheckoutData():
    # 获取公共参数,返回是 生成器，需转型
    commDatas = read_yaml("commondata_check.yml")
    commData = [i for i in commDatas]

    # 获取特别参数，返回是 生成器
    otherDatas = read_yaml("checkout_new.yml")
    casename = []
    param_one = []
    param_two = []
    mark = []
    for i in otherDatas:
        i["params_one"].update(commData[0]["comdata1"])
        i["params_two"].update(commData[0]["comdata2"])
        # 获取时间戳，生成 tr_transactionId
        t = time.time()
        i["params_one"]["transactionId"] = str(randint(0, 99999999)).zfill(8)

        # 组合待加签的数据
        # encryptData = i["params_one"]["merchantNo"] + i["params_one"]["subAccount"] + \
        #               i["params_one"]["transactionId"] + i["params_one"]["currency"] + \
        #               i["params_one"]["amount"] + i["params_one"]["firstName"] + \
        #               i["params_one"]["lastName"] + i["params_one"]["email"] + i["params_one"]["keys"]
        encryptData = i["params_one"]["merchantNo"] + i["params_one"]["subAccount"] + \
                      i["params_one"]["transactionId"] + i["params_one"]["currency"] + \
                      i["params_one"]["amount"] +i["params_one"]["returnUrl"] + i["params_one"]["keys"]

        sign = data_encrypt.dataEncrypt(encryptData)
        i["params_one"]["sign"] = sign

        casename.append(i["casenames"])
        param_one.append(i["params_one"])
        param_two.append(i["params_two"])
        marks = i["marks"]
        marklist = []
        for j in marks:
            marklist.append(tools.dicData[j])
        mark.append(marklist)
    allData = zip(casename, param_one, param_two, mark)
    # return list(allData)
    return dataToPytest(allData)


if __name__ == "__main__":
    a = getCheckoutData()
    print(a)
