import requests


class Api:
    dataSend = {
        "dataHash": "4B03196107C06132CECA4D8137B35B3694C957A01046EE0D2516AD9E2160BB30"
    }

    def send(self, data: dict):
        # 替换域名
        data["url"] = str(data["url"]).replace("testing-studio", "qjl-test.qianjinlian.com")

        requests.Request(method=data["method"], url=data["url"], headers=data["headers"], json="json")

    def send2(self):
        res = requests.post('https://qjl-test.qianjinlian.com/evidence/query', data=self.dataSend)
        return res.json()
