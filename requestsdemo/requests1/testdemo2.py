import requests

import env_demo


class TestApi():
    datasend2 = {
        "dataHash": "4B03196107C06132CECA4D8137B35B3694C957A01046EE0D2516AD9E2160BB30"
    }

    jsondata = {
        "dataHash": "4B03196107C06132CECA4D8137B35B3694C957A01046EE0D2516AD9E2160BB30"
    }

    data = {
        "method": "post",
        "url": "https://testing-studio/evidence/query",
        "headers": "Content-Type:application/json",
        "json": jsondata
    }

    def test_send(self):
        api = env_demo.Api()
        a = api.send(self.data)
        print(a)

    def test_send2(self):
        res = requests.post('https://qjl-test.qianjinlian.com/evidence/query', data=self.datasend2)
        print(res.status_code)
        # print(res.json())
