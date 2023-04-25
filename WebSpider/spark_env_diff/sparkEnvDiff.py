# -*- coding: UTF-8 -*-
import requests
from pyquery import PyQuery as pq

url1 = input('请输入第一个app id')
url2 = input('请输入第二个app id')


def get_html(url1, url2):
    return [pq(requests.get(url1).text)(
        '.aggregated-sparkProperties')('tbody')('td').items(), pq(requests.get(url2).text)(
        '.aggregated-sparkProperties')('tbody')('td').items()]


html = get_html(url1, url2)
# dic = {}
for i in html:
    try:
        while True:
            # dic[next(i).text()] = next(i).text()
            print(next(i).text(), '\t', next(i).text())
    except StopIteration:
        print("------------------------------")
        continue
