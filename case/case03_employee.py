import pytest
from tools import demo_positional
import time
import allure

_prize_code = None
_driver_employee = None


@allure.feature('员工核销模块')
class TestEmployee(object):

    @allure.story("获取核销码")
    def test_get_prize_code(self, _api, _domain, _methods):
        """
        获取核销码
        :param _api: 请求方法
        :param _domain: 域名
        :return:活动Id
        """
        global _prize_code

        data = _api.get_activity_code(_domain)

        _prize_code = data.json()['data']['list'][0]['writeOffCode']

        _methods.assert_code(data)

    @allure.story("初始化打开浏览器")
    def test_init_open_user(self):
        """初始化打开浏览器"""
        global _driver_employee

        _driver_employee = demo_positional.TestUi()
        _driver_employee.__int__("employee", "")

    @allure.story("登录页面-输入用户名")
    def test_send_username(self):
        """登录页面-输入用户名"""
        _driver_employee.by_xpath_send('//*[@id="app"]/div/div/section/div/div[2]/div[2]/div/input', '18512104952')

    @allure.story("登录页面-输入密码")
    def test_send_pwd(self):
        """登录页面-输入密码"""
        _driver_employee.by_xpath_send('//*[@id="app"]/div/div/section/div/div[3]/div[2]/div/input', '123456')

    @allure.story("登录页面-点击登录按钮")
    def test_click_login_button(self):
        """登录页面-点击登录按钮"""
        _driver_employee.by_js_driver('//*[@id="app"]/div/div/section/div/button/div')

    @allure.story("首页-点击核销按钮")
    def test_click_use_button(self):
        """首页-点击核销按钮"""
        _driver_employee.by_xpath_click('//*[@id="app"]/div[1]/div/section/div/div/div/div/div/a')

    @allure.story("核销页面-输入手机号")
    def test_send_phone(self):
        """核销页面-输入手机号"""
        _driver_employee.by_xpath_send('//*[@id="app"]/div/div/section/div/div[2]/div[1]/div[2]/div/input',
                                       '18512104952')

    @allure.story("核销页面-输入核销码")
    def test_send_prize_code(self):
        """核销页面-输入核销码"""
        _driver_employee.by_xpath_send('//*[@id="app"]/div/div/section/div/div[2]/div[2]/div[2]/div/input',
                                       _prize_code)

    @allure.story("点击提交核销")
    def test_click_use_submit(self):
        """点击提交核销"""

        _driver_employee.by_js_driver('//*[@id="app"]/div/div/section/div/div[2]/button/div/span')

    @allure.story("查看核销记录")
    def test_click_usre_record(self):
        """查看核销记录"""
        _driver_employee.by_xpath_click('//*[@id="app"]/div/div/section/div/div[1]/div[1]/div/div[2]')

        _driver_employee.by_xpath_click(
            '//*[@id="app"]/div/div/section/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/img')

    @allure.story("关闭浏览器")
    def test_close_driver(self):
        """关闭浏览器"""
        time.sleep(5)
        _driver_employee.close_driver()


if __name__ == '__main__':
    pytest.main()
