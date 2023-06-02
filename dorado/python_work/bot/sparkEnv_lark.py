# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq
import random

username = input('你的邮箱前缀:')
url1 = input('第一个addres(路径具体到environment):')
url2 = input('第二个addres(路径具体到environment):')
url = "https://open.feishu.cn/open-apis/bot/v2/hook/9e9844cc-7820-4a24-89ad-db1d6ca35218"


def send_lark(address, data, user_name):
    headers = {
        'Content-Type': 'application/json'
    }
    json = {
        'msg_type': 'interactive',
        'card': {
            'elements': [
                {
                    'tag': 'div',
                    'fields': [
                        {
                            'text': {
                                'content': '<at email=' + user_name + '@bytedance.com></at>',
                                'tag': 'lark_md',
                            }
                        },
                        {
                            'text': {
                                'tag': 'lark_md',
                                'content': '***三击以下文本可全选,复制到***:https://www.diffchecker.com/'
                            },
                            "is_short": False
                        }
                    ]
                }, {
                    'tag': 'hr',
                }, {
                    'tag': 'div',
                    'text': {
                        "content": data,
                        'tag': 'plain_text'
                    },
                }
            ],
            'header': {
                'title': {
                    'content': url1.split('/')[-3],
                    'tag': 'plain_text',
                },
                "template": random.choice(
                    ['blue', 'wathet', 'turquoise', 'green', 'yellow', 'orange', 'carmine', 'violet', 'indigo',
                     'purple'])
            },
        },
    }
    response = requests.post(address, headers=headers, json=json)
    print(response.text)


def get_html(url1, url2):
    return [pq(requests.get(url1).text)(
        '.aggregated-sparkProperties')('tbody')('td').items(), pq(requests.get(url2).text)(
        '.aggregated-sparkProperties')('tbody')('td').items()]


result = ''
for i in get_html(url1, url2):
    try:
        while True:
            result = result + next(i).text() + '\t' + next(i).text() + '\n'
    except StopIteration:
        send_lark(url, result, username)
        result = ''
        continue
