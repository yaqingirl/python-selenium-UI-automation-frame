#coding=utf-8
import re

from config.server_info import api_bookcity
import requests
import json
from util.getApiData import CollectionDetail

def getDataJson(collectionName):

    data={
        't': '1',
        'app':'jdread-m',
        'tm':'1562211771660',
        'os':'web',
        'client':'android',
        'uuid':'h516cf066b17b5ae98893a9e9cb00b1d02',
        'sign':'10e5fbff52b86832a7bcc000ed1b258a'
    }
    header={
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
    }
    response=requests.get(api_bookcity,params=data,headers=header)

    response_text=response.text

    response_data=json.loads(response_text)
    for item in response_data['data']:
        #普通的合集：展示的title和接口中的show_name一致的，例如："全网热销"
        object_str="'show_name': "+"'"+collectionName+"'"+", 'type"
        # a=str(item)
        if object_str in str(item):
            object_item = str(item)
            break
    else:
        #如果上面"普通的合集"没有匹配上，则按照以下方式匹配：title和接口中的show_name的前两个字一致的
        for item in response_data['data']:
            object_str = "'name': " + "'" + collectionName
            if object_str in str(item) and "作者专区" in str(item):
                object_item = str(item)
                break

        #如果上面两种方式都没有匹配到，那么就根据作者名字匹配，即title在作者列表里
        else:
            for item in response_data['data']:
                object_str = "'name': " + "'" + collectionName
                if object_str in str(item):
                    object_item = str(item)
                    break

            else:
                for item in response_data['data']:
                    object_str = "'show_name': " + "'" + collectionName[0:2]
                    if object_str in str(item):
                        object_item = str(item)
                        break
                else:
                    object_item=''


    if ''!=object_item:
        CollectionId=re.findall(r"{'collection_id': (\d+)",object_item)
        bookData=CollectionDetail.getDataJson(int(CollectionId[0]))
        return bookData
    else:
        return None

def getDataList(collectionName):

    data=getDataJson(collectionName)
    data_list=data['data']['items']

    return [item for item in data_list if "'ebook_id': 0" not in str(item)]

def getBookNameDataList(collectionName):
    books=getDataList(collectionName)
    namelist=[]
    for i in books:
        namelist.append(i['name'].replace(" ",""))
    return namelist

if __name__=="__main__":
    collectionName="本周特价"
    # collectionName = "经典回顾"
    data=getDataList(collectionName)
    for i in data:
        print(str(i['ebook_id'])+'：'+str(i['name']))



# https://jdread.jd.com/jdread/api/channel/100?app=jdread-m&tm=1562312273996&book_count=&os=web&client=android&uuid=h515fd70d30e89a84381c4db10c05a7c60&sign=4255bac2e57615adcc43be71e291b48d