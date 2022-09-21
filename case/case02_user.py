import pytest
from tools import demo_positional
import allure
import time

_activityId = None
_driver_user = None


@allure.feature('用户抽奖模块')
class TestUser(object):

    @allure.story("获取活动列表id")
    def test_get_activityList(self, _api, _domain, _methods):
        """
        获取活动列表id
        :param _api: 请求方法
        :param _domain: 域名
        :return:活动Id
        """
        global _activityId

        data = _api.get_activity_list(_domain)

        _activityId = data.json()['data']['list'][0]['id']

        _methods.assert_code(data)

    @allure.story("初始化打开浏览器")
    def test_init_open_user(self):
        """初始化打开浏览器"""
        global _driver_user

        _driver_user = demo_positional.TestUi()
        _driver_user.__int__("phone", str(_activityId))

    @allure.story("登录页面-输入用户名")
    def test_send_username(self):
        """登录页面-输入用户名"""
        _driver_user.by_xpath_send('//*[@id="appId"]/div/div[2]/div[2]/div/input', '18512104952')

    @allure.story("登录页面-输入密码")
    def test_send_pwd(self):
        """登录页面-输入密码"""
        _driver_user.by_xpath_send('//*[@id="appId"]/div/div[3]/div[2]/div/input', '123456')

    @allure.story("登录页面-点击登录按钮")
    def test_click_login_button(self):
        """登录页面-点击登录按钮"""
        _driver_user.by_js_driver('//*[@id="appId"]/div/button/div/span')

        _driver_user.by_js_driver('//*[@id="appId"]/div/div[1]/div/div[1]/div[2]/div[1]/div/canvas')

    @allure.story("登录页面-点击登录按钮")
    def test_click_prize_button(self):
        """抽奖活动页面-点击抽奖按钮"""
        _driver_user.by_mouse_click()

        time.sleep(7)

    @allure.story("点击个人中心按钮-进入个人中心页面")
    def test_click_user_info(self):
        """点击个人中心按钮-进入个人中心页面"""
        _driver_user.by_xpath_click('//*[@id="appId"]/div/div[2]/div/div[2]/div[1]')

        _driver_user.by_xpath_click('//*[@id="appId"]/div/div[2]/div/div[2]/div[1]')

    @allure.story("个人中心页面-点击中奖记录按钮")
    def test_check_prize_info(self):
        """个人中心页面-点击中奖记录按钮"""
        _driver_user.by_xpath_click('//*[@id="appId"]/div/div[1]/div/div/div[2]/div/div[1]')

        _driver_user.by_xpath_click('//*[@id="appId"]/div/div[2]/div[1]/div[1]/div[2]/div[1]/span')

    @allure.story("中奖记录列表-点击记录明细按钮查看明细")
    def test_check_prize_detail(self):
        """中奖记录列表-点击记录明细按钮查看明细"""
        _driver_user.by_xpath_click('//*[@id="appId"]/div/div[3]/div[2]/div/div/div[4]')

        _driver_user.by_xpath_click('//*[@id="appId"]/div/div[2]/div[1]/div[1]/div[2]/div[2]/span')

    @allure.story("关闭浏览器")
    def test_close_driver(self):
        """关闭浏览器"""
        _driver_user.close_driver()


if __name__ == '__main__':
    pytest.main()
