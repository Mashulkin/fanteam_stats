# -*- coding: utf-8 -*-
import requests


__author__ = 'Vadim Arsenev'
__version__ = '1.0.1'


class Parser(object):

    def __init__(self, url, *args):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/67.0.3396.79 Safari/537.36', }
        self.headers.update(*args)

    def get_response(self):
        """Connection to the site"""
        response = requests.get(self.url, headers=self.headers)
        response.encoding = 'utf-8'
        return response

    def get_pageData(self, response):
        """Getting json data"""
        try:
            data = response.json()
        except AttributeError as e:
            print(e)
            data = ''
        return data

    def parserResult(self):
        return self.get_pageData(self.get_response())
