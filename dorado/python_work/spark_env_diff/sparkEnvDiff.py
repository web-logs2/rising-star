# -*- coding: UTF-8 -*-
import requests
from requests import request

MEGATRON_HEADER = {"Authorization": "Bearer d8852e53cfffa6b57de50a8dba40d32a", "Domain": "megatron",
                   "Content-Type": "application/json"}
MEGATRON_APP_URL = 'https://paas-gw-boe.byted.org/api/v1/app/{app_id}'
SPARK_ENVIRONMENT_PATTERN = "{appUrl}/api/v1/applications/{appId}/{attemptId}/environment"


def getYarnResponse(region, url, method, headers):
    if region == "cn":
        return request(method=method, url=url, headers=headers).json()
    elif region == "va":
        return
    elif region == "sg":
        return
    else:
        return


def getAppRootUrl(appid, region):
    url_replace = MEGATRON_APP_URL.replace('{app_id}', appid)
    response = getYarnResponse(region, url_replace, 'get', MEGATRON_HEADER)
    # AMlog = response.get("data")[0].get('am_container_logs')
    lasUrl = response.get("data")[0].get('last_url')
    # if not ("mr-history" in AMlog) and not ("" == AMlog):
    #     AMlog = requests.get(AMlog).url
    if "history" in lasUrl and lasUrl[:4] == "http":
        return lasUrl.split('/history')[0]


def getSparkPropertis(rootUrl, appId):
    envUrl = SPARK_ENVIRONMENT_PATTERN.replace("{appUrl}", rootUrl).replace("{appId}", appId).replace("{attemptId}",
                                                                                                      "1")
    result = {}
    for i in requests.get(envUrl).json().get("sparkProperties"):
        result[i[0]] = i[1]
    return result


def diffConf(appId1,appId2,region):
    sparkRootUrl = getAppRootUrl(appId1, region)
    propertis = getSparkPropertis(sparkRootUrl, appId1)
    sparkRootUrl2 = getAppRootUrl(appId2, region)
    propertis2 = getSparkPropertis(sparkRootUrl2, appId2)




if __name__ == '__main__':
    region = input("请输入 region：")
    appId = input("请输入第一个 appid：")
    appId2 = input("请输入第二个 appid：")
    diffConf(appId1=appId,appId2=appId2,region=region)


