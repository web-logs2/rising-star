# -*- coding: utf-8 -*-
import requests
url = "https://paas-gw.byted.org/api/v1/app?app_id=application_1684899232999_3676808"
stage_url="/api/v1/applications/{appId}/stages"
payload={}
headers = {
   'Domain': 'megatron',
   'Authorization': 'Bearer fd0f8ab12b396f357a64e1a98a893112'
}

response = requests.request("GET", url, headers=headers, data=payload)
for i in response.json()['data'][0].items():
   print(i)
