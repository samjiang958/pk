import pytest
import allure
from tools import demo_positional

_driver_browser = None


@allure.feature('抽奖管理后台')
class Testcase(object):

    @allure.story("初始化方法打开浏览器")
    # @allure.severity(allure.severity_level.BLOCKER)
    # @allure.step('测试步骤')
    def test_init_open_admin(self):
        """初始化方法打开浏览器"""
        global _driver_browser

        _driver_browser = demo_positional.TestUi()
        _driver_browser.__int__("browser", "")

    @allure.story("登录页面-输入用户名")
    def test_send_username(self):
        """登录页面-输入用户名"""

        _driver_browser.by_name_send('username', "18512104952")

    @allure.story("登录页面-输入密码")
    def test_send_pwd(self):
        """登录页面-输入密码"""

        _driver_browser.by_name_send('password', "123456")

    @allure.story("登录页面-点击登录按钮")
    def test_click_login_button(self):
        """登录页面-点击登录按钮"""

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/div[1]/form/button')

    @allure.story("后台首页-点击导航栏")
    def test_click_navigation(self):
        """后台首页-点击导航栏"""

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div/li/div')

    @allure.story("后台首页-点击商品管理")
    def test_click_commodity(self):
        """后台首页-点击商品管理"""

        _driver_browser.by_class_click("el-menu-item")

    @allure.story("商品管理页-点击新增活动商品")
    def test_click_create_activity(self):
        """商品管理页-点击新增活动商品"""
        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/div/div[1]/button')

    @allure.story("新增活动页-输入活动名称")
    def test_send_activity_name(self, _methods):
        """新增活动页-输入活动名称"""

        _driver_browser.by_xpath_send('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div/div/input',
                                      "Ui自动化活动标题" + str(_methods.now_time()))

    @allure.story("新增活动页面-点击新增活动商品")
    def test_click_create_goods(self):
        """新增活动页面-点击新增活动商品"""
        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/div/button')

    @allure.story("新增商品弹框-选择商品类型")
    def test_click_goods_type(self):
        """新增商品弹框-选择商品类型"""
        _driver_browser.by_xpath_click('/html/body/div[2]/div/div[2]/form/div[1]/div/div/div/input')

        _driver_browser.by_xpath_click('/html/body/div[4]/div[1]/div[1]/ul/li[1]')

    @allure.story("新增商品弹框-选择商品模板")
    def test_click_goods_template(self):
        """新增商品弹框-选择商品模板"""

        _driver_browser.by_xpath_click('/html/body/div[2]/div/div[2]/form/div[2]/div/div/div/input')

        _driver_browser.by_xpath_click('/html/body/div[5]/div[1]/div[1]/ul/li[1]')

    @allure.story("新增商品弹框-输入中奖概率")
    def test_click_probability(self):
        """新增商品弹框-输入中奖概率"""

        _driver_browser.by_xpath_send('/html/body/div[2]/div/div[2]/form/div[3]/div/div/div/input', "20")

    @allure.story("新增商品弹框-点击提交按钮")
    def test_click_create_goods_button(self):
        """新增商品弹框-点击提交按钮"""
        _driver_browser.by_xpath_click('/html/body/div[2]/div/div[3]/div/button[2]')

    @allure.story("新增活动页面-点击新增活动商品2")
    def test_click_create_goods2(self):
        """新增活动页面-点击新增活动商品2"""

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/div/button')

    @allure.story("新增商品弹框-选择商品类型2")
    def test_click_goods_type2(self):
        """新增商品弹框-选择商品类型2"""

        _driver_browser.by_xpath_click('/html/body/div[5]/div/div[2]/form/div[1]/div/div/div/input')

        _driver_browser.by_xpath_click('/html/body/div[5]/div[1]/div[1]/ul/li[1]')

    @allure.story("新增商品弹框-选择商品模板2")
    def test_click_goods_template2(self):
        """新增商品弹框-选择商品模板2"""

        _driver_browser.by_xpath_click('/html/body/div[4]/div/div[2]/form/div[2]/div/div/div/input')

        _driver_browser.by_xpath_click('/html/body/div[5]/div[1]/div[1]/ul/li[2]')

    @allure.story("新增商品弹框-输入中奖概率2")
    def test_click_probability2(self):
        """新增商品弹框-输入中奖概率2"""

        _driver_browser.by_xpath_send('/html/body/div[3]/div/div[2]/form/div[3]/div/div/div/input', "30")

    @allure.story("新增商品弹框-点击提交按钮")
    def test_click_create_goods_button2(self):
        """新增商品弹框-点击提交按钮"""
        _driver_browser.by_xpath_click('/html/body/div[3]/div/div[3]/div/button[2]')

    @allure.story("新增活动页面-点击新增活动商品3")
    def test_click_create_goods3(self):
        """新增活动页面-点击新增活动商品3"""

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/form/div[5]/div/div/button')

    @allure.story("新增商品弹框-选择商品类型3")
    def test_click_goods_type3(self):
        """新增商品弹框-选择商品类型3"""
        _driver_browser.by_xpath_click('/html/body/div[5]/div/div[2]/form/div[1]/div/div/div/input')

        _driver_browser.by_xpath_click('/html/body/div[5]/div[1]/div[1]/ul/li[1]')

    @allure.story("新增商品弹框-选择商品模板3")
    def test_click_goods_template3(self):
        """新增商品弹框-选择商品模板3"""
        _driver_browser.by_xpath_click('/html/body/div[4]/div/div[2]/form/div[2]/div/div/div/input')

        _driver_browser.by_xpath_click('/html/body/div[5]/div[1]/div[1]/ul/li[3]')

    @allure.story("新增商品弹框-输入中奖概率3")
    def test_click_probability3(self):
        """新增商品弹框-输入中奖概率3"""
        _driver_browser.by_xpath_send('/html/body/div[3]/div/div[2]/form/div[3]/div/div/div/input', "40")

    @allure.story("新增商品弹框-点击提交按钮")
    def test_click_create_goods_button3(self):
        """新增商品弹框-点击提交按钮"""
        _driver_browser.by_xpath_click('/html/body/div[3]/div/div[3]/div/button[2]')

    @allure.story("新增活动页-点击新增失败提示语")
    def test_click_Defeat_ext_button(self):
        """新增活动页-点击新增失败提示语"""
        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/form/div[8]/button')

    @allure.story("新增失败提示语弹框-添加失败提示文案")
    def test_send_Defeat_text(self):
        """新增失败提示语弹框-添加失败提示文案"""
        _driver_browser.by_xpath_send('/html/body/div[5]/div/div[2]/form/div[1]/div/div[1]/input',
                                      "很遗憾未中奖,再接再厉哦")

    @allure.story("新增失败提示语弹框-添加失败概率")
    def test_send_Defeat_probability(self):
        """新增失败提示语弹框-添加失败概率"""
        _driver_browser.by_xpath_send('/html/body/div[5]/div/div[2]/form/div[2]/div/div/div/input', "10")

    @allure.story("新增失败提示语弹框-点击提交按钮")
    def test_click_creat_button(self):
        """新增失败提示语弹框-点击提交按钮"""
        _driver_browser.by_xpath_click('/html/body/div[5]/div/div[3]/div/button[2]')

    @allure.story("新增活动页面-点击提交按钮")
    def test_click_create_activity_button(self):
        """新增活动页面-点击提交按钮"""
        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/form/div[10]/button[2]')

    @allure.story("活动管理页-根据活动名称模糊搜索")
    def test_get_activityName_list(self):
        """活动管理页-根据活动名称模糊搜索"""
        _driver_browser.by_xpath_send('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[2]/div/input',
                                      "Ui自动化活动标题")

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[3]/button[1]')

    @allure.story("活动管理页面-根据活动状态搜索")
    def test_get_activityStatus_list(self):
        """活动管理页面-根据活动状态搜索"""
        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[1]/div/div/input')

        _driver_browser.by_xpath_click('/html/body/div[2]/div[1]/div[1]/ul/li[2]')

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[3]/button[1]')

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[1]/div/div/input')

        _driver_browser.by_xpath_click('/html/body/div[2]/div[1]/div[1]/ul/li[3]')

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[3]/button[1]')

    @allure.story("活动管理页面-点击启用活动按钮")
    def test_click_start_activityStatus(self):
        """活动管理页面-点击启用活动按钮"""
        _driver_browser.by_xpath_click(
            '//*[@id="app"]/div/div[2]/section/div/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/div/div')

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[1]/div/div/input')

    @allure.story("商品管理页-重置搜索内容")
    def test_clear_activity_list(self):
        """商品管理页-重置搜索内容"""
        _driver_browser.by_xpath_click('/html/body/div[2]/div[1]/div[1]/ul/li[1]')

        _driver_browser.by_xpath_clear('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[2]/div/input')

        _driver_browser.by_xpath_click('//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[3]/button[1]/i')

    @allure.story("关闭浏览器")
    def test_close_driver(self):
        """关闭浏览器"""

        _driver_browser.close_driver()


if __name__ == '__main__':
    pytest.main()
