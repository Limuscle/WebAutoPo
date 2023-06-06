import base64
import json
import requests


class TestApiRequest:
    req_data = {
        "method": "get",
        "url": "www.sdf.com",
        "headers": None,
        "encodings": "base64"
    }

    def test_demo1(self, data: dict):
        r = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64encode(r.content))

        # 不是通用算法，且开发无法提供解密，需要把加密过后的结果返送给第三方进行解密
        elif data["encoding"] == "private":
            return requests.post("url", data=r.content)
