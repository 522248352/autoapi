import time
from random import randint


import tools
from tools import data_encrypt
from tools.data2pytest import dataToPytest
from tools.read_yaml import read_yaml


def getSaleData():

    # 获取公共参数,返回是 生成器，需转型
    commDatas = read_yaml("commondata_sale.yml")
    commData = [i for i in commDatas]

    # 获取特别参数，返回是 生成器
    otherDatas = read_yaml("sale.yml")
    casename = []
    data = []
    mark = []
    for i in otherDatas:
        # 获取时间戳，生成 tr_no
        i["datas"].update(commData[0])
        t = time.time()
        i["datas"]["transactionId"] = str(randint(0, 99999999)).zfill(8)

        # 组合待加签的数据
        encryptData = i["datas"]["merchantNo"] + i["datas"]["subAccount"] + \
                      i["datas"]["transactionId"] + i["datas"]["currency"] + \
                      i["datas"]["amount"] + i["datas"]["firstName"] + \
                      i["datas"]["lastName"] + i["datas"]["cardNumber"] + \
                      i["datas"]["year"] + i["datas"]["month"] + i["datas"]["cvv"] + \
                      i["datas"]["email"] + i["datas"]["keys"]

        sign = data_encrypt.dataEncrypt(encryptData)    
        i["datas"]["sign"] = sign
        
        casename.append(i["casenames"])
        data.append(i["datas"])
        marks = i["marks"]
        markList = []
        for j in marks:
            markList.append(tools.dicData[j])
        mark.append(markList)
    allData =  zip(casename, data, mark)
    return dataToPytest(allData)

if __name__ == "__main__":
    a = getSaleData()
    for i in a:
        print(i)