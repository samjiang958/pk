# from tools import read_json
import requests
import json
import re


class ApiRequests(object):

    def post_api(self, url, para):
        """
        post 请求
        url: 请求接口
        para: 请求参数
        """
        head = {

            "token": "18512104952"
        }
        api = requests.post(url, json=para, headers=head)

        return api

    def get_api(self, url):
        """
        post 请求
        url: 请求接口
        para: 请求参数
        """
        head = {

        }
        api = requests.get(url, headers=head)

        return api

    def put_post_api(self, url, para):
        """
        post 请求
        url: 请求接口
        para: 请求参数
        """

        head = {

        }
        api = requests.put(url, json=para, headers=head)

        return api

    def put_get_api(self, url):
        """
        post 请求
        url: 请求接口
        para: 请求参数
        """
        head = {

        }
        api = requests.put(url, headers=head)

        return api
