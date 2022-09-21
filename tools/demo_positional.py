import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 手机模式
import win32api
import win32con
import pyautogui


class TestUi(object):

    def __int__(self, model, num):

        if model == "browser":

            self.driver = webdriver.Chrome()

            self.driver.get("http://mfpkfb01.cmcr.vip")

            # self.driver.get("https://baidu.com")

            time.sleep(1)

            self.driver.maximize_window()

            self.driver.implicitly_wait(30)

        elif model == "phone":

            # 设置手机型号，这设置为iPhone 6
            mobile_emulation = {"deviceName": "iPhone 6"}

            options = Options()
            options.add_experimental_option("mobileEmulation", mobile_emulation)

            # 启动配置好的浏览器
            self.driver = webdriver.Chrome(options=options)

            url = "http://mfpkfb02.cmcr.vip/#/login?activityId=" + num
            # 输入网址
            self.driver.get(url)
            time.sleep(1)

            self.driver.maximize_window()

            self.driver.implicitly_wait(30)

        else:

            # 设置手机型号，这设置为iPhone 6
            mobile_emulation = {"deviceName": "iPhone 6"}

            options = Options()
            options.add_experimental_option("mobileEmulation", mobile_emulation)

            # 启动配置好的浏览器
            self.driver = webdriver.Chrome(options=options)

            url = "http://mfpkfb03.cmcr.vip/#/home-index"
            # 输入网址
            self.driver.get(url)
            time.sleep(1)

            self.driver.maximize_window()

            self.driver.implicitly_wait(30)

    def by_id_click(self, path):
        self.wait_time()
        self.driver.find_element(By.ID, path).click()

    def by_id_send(self, path, key):
        self.wait_time()
        self.driver.find_element(By.ID, path).send_keys(key)

    def by_xpath_click(self, path):
        self.wait_time()
        self.driver.find_element(By.XPATH, path).click()

    def by_xpath_send(self, path, key):
        self.wait_time()
        self.driver.find_element(By.XPATH, path).send_keys(key)

    def by_xpath_clear(self, path):
        self.wait_time()
        self.driver.find_element(By.XPATH, path).clear()

    def by_xpath_text(self, path):
        self.wait_time()
        return self.driver.find_element(By.XPATH, path).text

    def by_name_click(self, path):
        self.wait_time()
        self.driver.find_element(By.NAME, path).click()

    def by_name_send(self, path, key):
        self.wait_time()
        self.driver.find_element(By.NAME, path).send_keys(key)

    def by_class_click(self, path):
        self.wait_time()
        self.driver.find_element(By.CLASS_NAME, path).click()

    def by_class_send(self, path, key):
        self.wait_time()
        self.driver.find_element(By.CLASS_NAME, path).send_keys(key)

    def by_js_driver(self, path):
        self.wait_time()
        zbxx = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script('arguments[0].click()', zbxx)

    def close_driver(self):
        self.wait_time()
        self.driver.close()
        self.driver.quit()

    def by_mouse_click(self):
        time.sleep(3)
        pyautogui.moveTo(283, 538, duration=1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def wait_time(self):

        time.sleep(1)





if __name__ == '__main__':
    case = TestUi()

    case.__int__("browser", "")

