from tools import api_request
class PkApi(object):

    def __init__(self):

        self.api = api_request.ApiRequests()

    def get_activity_list(self, domain):
        """
        获取活动列表ID
        :param domain:域名
        :return:接口返回
        """

        url = domain + "/manager/selectActivityList"

        para = {
            "pageNum": 1,
            "pageSize": 10
        }
        data = self.api.post_api(url,para)

        return data

    def get_activity_code(self, domain):
        """
        获取中奖信息
        :param domain:域名
        :return:接口返回
        """

        url = domain + "/user/prizeMyList"

        para = {
            "pageNum": 1,
            "pageSize": 10
        }
        data = self.api.post_api(url,para)

        return data



if __name__ == '__main__':
    print(PkApi().get_activity_code("http://mfpkb.cmcr.vip").json()['data']['list'][0]['id'])
