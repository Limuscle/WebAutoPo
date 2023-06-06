from web.qjlBackend.login_page import LoginPage


class TestRegister:
    def setup(self):
        self.login = LoginPage()

    def test_login(self):
        # 登录
        assert self.login.goto_index()

    def test_resetPassword(self):
        # 重置密码
        assert self.login.goto_resetPassword()

    def test_resetAndLogin(self):
        assert self.login.goto_resetPassword().goto_index()
