import requests
from requests.auth import HTTPBasicAuth

'''
见证接口
'''


# 获取数据包接口
def getPacketsFun(witnessUrl, witnessAuto, witnessdata):
    return requests.post(witnessUrl + "/witness/getPackets", json=witnessdata,
                         auth=HTTPBasicAuth(witnessAuto['Username'], witnessAuto['Password']))


# APP用户见证接口
def signatureFun(witnessUrl, witnessAuto, witnessdata):
    return requests.post(witnessUrl + "/witness/signature", json=witnessdata,
                         auth=HTTPBasicAuth(witnessAuto['Username'], witnessAuto['Password']))


# 获取包明细信息
def packetDetailFun(witnessUrl, witnessAuto, witnessdata):
    return requests.post(witnessUrl + "/witness/packet/detail", json=witnessdata,
                         auth=HTTPBasicAuth(witnessAuto['Username'], witnessAuto['Password']))


# 获取数据包见证数据
def packetWitnessListFun(witnessUrl, witnessAuto, witnessdata):
    return requests.post(witnessUrl + "/witness/packet/witnessList", json=witnessdata,
                         auth=HTTPBasicAuth(witnessAuto['Username'], witnessAuto['Password']))


# 获取用户见证信息
def userWitnessListFun(witnessUrl, witnessAuto, witnessdata):
    return requests.post(witnessUrl + "/witness/user/witnessList", json=witnessdata,
                         auth=HTTPBasicAuth(witnessAuto['Username'], witnessAuto['Password']))


# 数据包见证信息统计-只有未见证的数据
def packetsStatisticsFun(witnessUrl, witnessAuto, witnessdata):
    return requests.post(witnessUrl + "/witness/packets/statistics", json=witnessdata,
                         auth=HTTPBasicAuth(witnessAuto['Username'], witnessAuto['Password']))
