import random
import datetime
import time


class Methods(object):

    def now_time(self):
        """获取时间"""
        return (datetime.datetime.now() + datetime.timedelta(minutes=0)).strftime("%Y-%m-%d %H:%M:%S")

    def wait_time(self,num):

        time.sleep(num)

    def random_number(self, x, d):
        """
        随机数
        X：最小随机数 >=X
        D：最大随机数 <=D
        """
        d -= 1

        return random.randint(x, d)

    def assert_code(self, api):
        """
        状态码断言

        :return:
        """
        assert 200 == api.status_code
