import requests
from requests.auth import HTTPBasicAuth
'''
存证接口
'''


# 域名路由不同/evidence/cochain
def CochainFun(CochainFunUrl, CochainFunHeaders, CochainFundata, CochainFunAuto):
    res = requests.post(CochainFunUrl + "/evidence/cochain", headers=CochainFunHeaders, json=CochainFundata, auth=HTTPBasicAuth(CochainFunAuto['Username'], CochainFunAuto['Password']))
    return res


# 域名路由不同/evidence/base64/cochain
def base64CochainFun(CochainFunUrl, CochainFunHeaders, CochainFundata, CochainFunAuto):
    res = requests.post(CochainFunUrl + "/evidence/base64/cochain", headers=CochainFunHeaders, json=CochainFundata, auth=HTTPBasicAuth(CochainFunAuto['Username'], CochainFunAuto['Password']))
    return res
