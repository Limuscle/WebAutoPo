import allure
import pytest
import yaml
from requestsdemo.qjlApiEvidence import cochain, witness


# 存证接口测试
class Testqjl:
    '''
    从testdata的yml文件中读取测试数据
    '''
    @pytest.mark.parametrize('cochaindata', yaml.safe_load(open("testData/ba16CochainFun.yaml", encoding="utf-8")))
    def test_ba16CochainFun(self, cochaindata):
        # 测试存证接口，16进制公私钥，dataVersion版本
        r = cochain.CochainFun(cochaindata['CochainFunUrl'], cochaindata['CochainFunHeaders'], cochaindata['CochainFundata'], cochaindata['CochainFunAuto'])
        if cochaindata['CochainFunAuto']['Username'] == 'qjl-jchain@auth_test1':
            with allure.step('Auto账号错误'):
                assert r.status_code == 401
        elif cochaindata['CochainFunAuto']['Password'] == 'qjl-jchain@20231':
            with allure.step('Auto密码错误'):
                assert r.status_code == 401
        else:
            if r.json()['message'] == '重复请求':
                with allure.step('重复请求'):
                    print(r.json()['message'])
                    assert r.json()['message'] == '重复请求'
            else:
                with allure.step('正常请求,存证上链'):
                    assert r.json()['code'] == 0
                    assert r.json()['message'] == '操作成功'

    @pytest.mark.parametrize('cochaindata', yaml.safe_load(open("testData/ba16version.yaml", encoding="utf-8")))
    def test_ba16CochainFunVersion(self, cochaindata):
        # 测试存证接口，16进制公私钥，version版本
        r = cochain.CochainFun(cochaindata['CochainFunUrl'], cochaindata['CochainFunHeaders'], cochaindata['CochainFundata'], cochaindata['CochainFunAuto'])
        assert r.json()['code'] == 0
        assert r.json()['message'] == '操作成功'

    @pytest.mark.parametrize('cochaindata', yaml.safe_load(open("testData/base64fun.yaml", encoding="utf-8")))
    def test_base64CochainFun(self, cochaindata):
        # 测试存证接口，base64进制公私钥
        r = cochain.base64CochainFun(cochaindata['CochainFunUrl'], cochaindata['CochainFunHeaders'], cochaindata['CochainFundata'], cochaindata['CochainFunAuto'])
        assert r.json()['code'] == 0
        assert r.json()['message'] == '操作成功'

    @pytest.mark.parametrize('cochaindata', yaml.safe_load(open("testData/base64versionfun.yaml", encoding="utf-8")))
    def test_base64CochainFunVersion(self, cochaindata):
        # 测试存证接口，base64进制公私钥，version版本
        r = cochain.base64CochainFun(cochaindata['CochainFunUrl'], cochaindata['CochainFunHeaders'], cochaindata['CochainFundata'], cochaindata['CochainFunAuto'])
        assert r.json()['code'] == 0
        assert r.json()['message'] == '操作成功'

# 见证相关接口测试
    # @classmethod
    @pytest.mark.parametrize('witnessdata', yaml.safe_load(open("testData/getPacketsData.yaml", encoding="utf-8")))
    def test_getPacketsFun(self, witnessdata):
        # 测试见证接口，获取数据包
        r = witness.getPacketsFun(witnessdata['witnessUrl'], witnessdata['witnessAuto'], witnessdata['witnessData'])
        assert r.json()['code'] == 0
        assert r.json()['message'] == '操作成功'

    @pytest.mark.parametrize('witnessdata', yaml.safe_load(open("testData/signatureData.yaml", encoding=" utf-8")))
    def test_signatureFun(self, witnessdata):
        # 测试见证接口，APP用户见证接口
        r = witness.signatureFun(witnessdata['witnessUrl'], witnessdata['witnessAuto'], witnessdata['witnessData'])
        print(r.text)
        print(r.status_code)

    @pytest.mark.parametrize('witnessdata', yaml.safe_load(open("testData/packetDetailData.yaml", encoding=" utf-8")))
    def test_packetDetailFun(self, witnessdata):
        # 测试见证接口，获取包明细信息
        r = witness.packetDetailFun(witnessdata['witnessUrl'], witnessdata['witnessAuto'], witnessdata['witnessData'])
        assert r.json()['code'] == 0
        assert r.json()['message'] == '操作成功'

    @pytest.mark.parametrize('witnessdata', yaml.safe_load(open("testData/packetWitnessListData.yaml", encoding=" utf-8")))
    def test_packetWitnessListFun(self, witnessdata):
        # 测试见证接口，获取数据包见证数据
        r = witness.packetWitnessListFun(witnessdata['witnessUrl'], witnessdata['witnessAuto'], witnessdata['witnessData'])
        assert r.json()['code'] == 0
        assert r.json()['message'] == '操作成功'

    @pytest.mark.parametrize('witnessdata', yaml.safe_load(open("testData/userWitnessListData.yaml", encoding=" utf-8")))
    def test_userWitnessListFun(self, witnessdata):
        # 测试见证接口，获取用户见证信息
        r = witness.userWitnessListFun(witnessdata['witnessUrl'], witnessdata['witnessAuto'], witnessdata['witnessData'])
        assert r.json()['code'] == 0
        assert r.json()['message'] == '操作成功'

    @pytest.mark.parametrize('witnessdata', yaml.safe_load(open("testData/packetsStatisticsData.yaml", encoding=" utf-8")))
    def test_packetsStatisticsFun(self, witnessdata):
        # 测试见证接口，数据包见证信息统计
        r = witness.packetsStatisticsFun(witnessdata['witnessUrl'], witnessdata['witnessAuto'], witnessdata['witnessData'])
        assert r.json()['code'] == 0
        assert r.json()['message'] == '操作成功'

