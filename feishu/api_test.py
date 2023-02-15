import requests
import json

url = "https://open.feishu.cn/open-apis/bot/v2/hook/7767f288-01d6-4aba-b768-527921b409bd"
url1 = "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id"
payload = json.dumps({
    "content": "{\"text\":\"<at user_id=\\\"ou_5a22d939102e78039e47f360dc21950e\\\"></at> API test\"}",
    "msg_type": "text",
    "receive_id": "ou_5a22d939102e78039e47f360dc21950e"
})

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer t-g1049lauQ5Z5NZLWGHCCMHHXQ7DV5EKRNRNBKLOF'
}

response = requests.request("POST", url1, headers=headers, data=payload)
print(response.text)

