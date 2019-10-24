#coding=utf-8
import re

from config.server_info import api_collection
import requests
import json

def getDataJson(collectId):

    data={
        't': '1',
        'app':'jdread-m',
        'tm':'1562211771660',
        'page':'1',
        'page_size':'12',
        'os':'web',
        'client':'android',
        'uuid':'h516cf066b17b5ae98893a9e9cb00b1d02',
        'sign':'10e5fbff52b86832a7bcc000ed1b258a'
    }
    data['collectId']=collectId
    header={
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
    }
    url=api_collection+'/'+str(collectId)
    response=requests.get(url,params=data,headers=header)
    # book_list=re.findall(r'"ebook_id":(\d+)',response.text)
    result=json.loads(response.text)
    return result


if __name__=="__main__":

    collectId=2430
    print(getDataJson(collectId))
    print(type(getDataJson(collectId)))

# https://jdread.jd.com/jdread/api/channel/100?app=jdread-m&tm=1562312273996&book_count=&os=web&client=android&uuid=h515fd70d30e89a84381c4db10c05a7c60&sign=4255bac2e57615adcc43be71e291b48d