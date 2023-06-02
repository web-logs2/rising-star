# coding: utf-8
import requests

# ou_fadcef3b3fcce74080f53cc470393883
# img_v2_d482425c-b65b-4fb3-889c-83d447c3d65g

url = "https://open.feishu.cn/open-apis/bot/v2/hook/9e9844cc-7820-4a24-89ad-db1d6ca35218"
headers = {
    'Content-Type': 'application/json'
}

interactive = {
    'msg_type': 'interactive',
    'card': {
        'elements': [
            {
                'text': {
                    "content": "Content module",
                    'tag': 'plain_text'
                },
                'tag': 'div',
                'fields': [
                    {
                        'text': {
                            'content': '<at email=duanze@bytedance.com></at>',
                            'tag': 'lark_md',
                        }
                    },
                    {
                        'text': {
                            'tag': 'lark_md',
                            'content': "***text*** aaa"
                        },
                        "is_short": False
                    }
                ]
            },
            {
                'tag': 'hr',  # 分割线
            },
            {
                'tag': 'div',
                'text': {
                    "content": "Content module",
                    'tag': 'plain_text'
                }
            }

        ],
        'header': {
            'title': {
                'content': 'addres！！！',
                'tag': 'plain_text',
            },
            "template": "indigo"
        },
    },
}
image = {
    "msg_type": "image",
    "content": {"image_key": "img_v2_d482425c-b65b-4fb3-889c-83d447c3d65g"}
}
text = {
    "content": {
        "text": "普通文本测试\n<b>粗体</b>\t<i>斜体</i>\t<u>下划线</u>\t<s>删除线</s>\n[飞书超链接](https://open.feishu.cn)"
    },
    "msg_type": "text"
}
post = {
    "msg_type": "post",
    "content": {
        "post": {
            "zh_cn": {
                "title": "我是一个标题",
                "content": [
                    [  # 一个列表一行
                        {
                            "tag": "text",
                            "text": "第一行:",
                        },
                        {
                            "tag": "a",
                            "href": "https://www.feishu.cn",
                            "text": "飞书开放平台",
                        },
                        {
                            "tag": "at",
                            "user_id": "ou_fadcef3b3fcce74080f53cc470393883",
                        }
                    ],
                    [
                        {
                            "tag": "text",
                            "text": "第二行:\t",
                        },
                        {
                            "tag": "text",
                            "text": "图片会独占一行",
                        },
                        {
                            "tag": "img",
                            "image_key": "img_v2_d482425c-b65b-4fb3-889c-83d447c3d65g"
                        }
                    ],
                    [
                        {
                            "tag": "text",
                            "text": "第三行:",
                        },
                        {
                            "tag": "text",
                            "text": "文本测试"
                        }
                    ]
                ]
            }
        }
    }
}
response = requests.post(url, headers=headers, json=interactive)
print(response.text)
